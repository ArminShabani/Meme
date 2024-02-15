class Meme_database:
    def __init__(self, name, genre, date, description, id, database={}, flag=0):
        self.name = name
        self.genre = genre
        self.date = date
        self.description = description
        self.id = id
        self.flag = flag
        database.update({id: [self.name, self.genre, self.date, self.description]})
        self.decoy = database
        if self.id != 1:
            database = self.decoy

        for i in range(1, self.id + 1):
            if database[i] != []:
                if database[i][0] == self.name and i != self.id:
                    self.flag = 1
                    print("\nDuplicate<meme name>\n")
                    database.pop(self.id)
                    break
                else:
                    continue
            else:
                continue
        if self.flag == 0:
            print("\nYour request has been successfully sent to Azizi\n")
        self.decoy = database

    def flag(self):
        if self.flag == 1:
            return 1
        elif self.flag == 0:
            return 0

    def deleter(self, name):
        flag = 0
        for i in range(1, self.id + 1):
            if self.decoy[i] != []:
                if self.decoy[i][0] == name:
                    print("\nMeme deleted successfully\n")
                    flag = 1
                    self.decoy[i] = []
                    break
            else:
                continue
        if flag == 0:
            print("\nThis meme is not available\n")
        return flag

    def requests(self):
        flag = 1
        k = 1
        for i in range(1, self.id + 1):
            if self.decoy[i] != []:
                flag = 2
                print(f"\nYour request {k} is about {self.decoy[i][0]}, which its genre is {self.decoy[i][1]}, you "
                      f"will recieve the meme on {self.decoy[i][2]}, and your description is: {self.decoy[i][3]}\n")
                k+=1
        if flag == 1:
            print("\nNo request has been registered\n")


id = 1
while True:

    print("what do you want to do darling??")
    print("If you have any request for meme, press 1 ")
    print("If you regret, press 2")
    print("If you want to see your requests, press3")
    print("If you want to see your information, press4")
    print("If you want to change your information, press5")
    print("And for logging out, press 6")
    a = input()

    match a:
        case '1':
            while True:
                meme_name = input("please enter the name of your meme:")
                meme_genre = input("please enter the genre of your meme:")
                meme_date = input("please enter the maximum receive date of your meme:")
                meme_description = input("please add some description:")
                meme_id = id
                user = Meme_database(meme_name, meme_genre, meme_date, meme_description, meme_id)
                flag = user.flag
                if flag == 0:
                    id += 1
                    break

        case '2':
            meme_name = input("please enter your meme name:")
            k = user.deleter(meme_name)

        case '3':
            user.requests()

        case '4':

            pass
        case '5':

            pass
        case '6':
            exit()
        case _:
            print("please enter a valid number")

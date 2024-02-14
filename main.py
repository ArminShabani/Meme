class Meme_database:
    def __init__(self, name, genre, date, description, id, database={}, flag=0):
        self.name = name
        self.genre = genre
        self.date = date
        self.description = description
        self.id = id
        self.flag = flag
        database.update({id: [self.name, self.genre, self.date, self.description]})
        for i in range(1, self.id + 1):
            if database[i][0] == self.name and i != self.id:
                self.flag = 1
                print("Duplicate<meme name>")
                database.pop(self.id)
                break
            else:
                continue
        if self.flag == 0:
            print("Your request has been successfully sent to Azizi")
        print(database)

    def flag(self):
        if self.flag == 1:
            return 1
        elif self.flag == 0:
            return 0



id = 1
while True:
    print("what do you want to do darling??")
    print("If you have any request for meme, press 1 ")
    print("If you regret, press 2")
    print("If you want to see your requests, press3")
    print("If you want to see your information, press4")
    print("If you want to change your information, press5")
    print("If you want to be yam yam, press 6")
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

        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            exit()
        case _:
            print("gavi???")
            print("man daram inja zahmat mikesham")
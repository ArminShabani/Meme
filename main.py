import os #operating system
import datetime #date and time
class MainDataBase:
    def __init__(self):
        self.users = []
        self.usernames = []
        self.emails = []
    def login(self,id,username,password):
        if username in self.usernames:
            for i in self.users:
                if i.username == username and i.password == password:
                    i.id = id
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'welcome {username} with id {id-1}')
                    return True
        else:
            print("invalid Credentials")
    
    def register(self,id,firstname,lastname,email,username,password,re_password):
        if username not in self.usernames and email not in self.emails:
            if password == re_password:
                self.id = id
                self.emails.append(email)
                self.usernames.append(username)
                self.users.append(Users(id,firstname,lastname,email,username,password))
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{username} has been succesfully submited with id of {id}")
                return True
            else:
                print("Password do not match")
                return False
        else:
            print("Username or Email already exists. Please try again.")
            return False

   
    def view_user_info(self, id):
        for user in self.users:
            if user.id == id+1:
                return user
        print(f"no user was found with that id of {id}")
    


    def update_user(self,username,password,new_entry,field):
        for i in self.users:
            if i.username == username and i.password == password:
                if field == "username":
                    i.username = new_entry
                    self.usernames.remove(username)
                    self.usernames.append(new_entry)
                    return True
                elif field == "password":
                    i.password = new_entry
                    return True
                else:
                    print("invalid field")
                    return False
class Users:
    def __init__(self,id,firstname,lastname,email,username,password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
    def __str__(self):
        return f"Id: {self.id -1}, Name: {self.firstname} {self.lastname}, Email: {self.email}, Username: {self.username}"


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
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nDuplicate<meme name>\n")
                    database.pop(self.id)
                    break
                else:
                    continue
            else:
                continue
        if self.flag == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nMeme deleted successfully\n")
                    flag = 1
                    self.decoy[i] = []
                    break
            else:
                continue
        if flag == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nThis meme is not available\n")
        return flag

    def requests(self):
        flag = 1
        k = 1
        for i in range(1, self.id + 1):
            if self.decoy[i] != []:
                flag = 2
                print(f"\nYour request {k} is about {self.decoy[i][0]}, which its genre is {self.decoy[i][1]}, you "
                      f"meme has been submited on {self.decoy[i][2]}, and your meme description is: {self.decoy[i][3]}\n")
                k+=1
        if flag == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nNo request has been registered\n")
            
            

def main():
    user_id = 1
    meme_id = 1
    mainDataBase = MainDataBase()
    login_Success = False
    register_Success = False
    logout_flag = False
    change = False
    while True:
        print("welcome")
        print("1.register")
        print("2.login")
        print("3.exit")
        try:
            choice = int(input("Enter a number (1/2/3): "))
            if choice == 2:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                login_Success = mainDataBase.login(user_id,username,password) 
                if login_Success == False:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("invalid credentials. Please try again.")
            elif choice == 1:
                print(f"your account id is {user_id}")
                id = user_id
                name = input("State your First name: ")
                second_name = input("State your Last Name: ")
                email = input("Enter your email: ")
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                re_password = input("Re-enter your password: ")
                register_Success = mainDataBase.register(id,name,second_name,email,username,password,re_password)
                if register_Success:
                    user_id += 1
                else :
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("invalid credentials")
                    login_Success = False
            elif choice == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thanks for useing our application")
                exit()
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Enter a valid number from (1/2/3)")
        if login_Success:
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
                            meme_date = datetime.datetime.now(datetime.UTC)
                            meme_description = input("please add some description:")
                            id = meme_id
                            user = Meme_database(meme_name, meme_genre, meme_date, meme_description, id)
                            flag = user.flag
                            if flag == 0:
                                meme_id += 1
                                break
    
                    case '2':
                        meme_name = input("please enter your meme name:")
                        user.deleter(meme_name)
                    case '3':
                        user.requests()
                    case '4':
                        user_choice=int(input("enter your id please:")) 
                        print(mainDataBase.view_user_info(user_choice))
                    case '5':
                        field_choice = input("which field do you want to change?(username/password)")
                        entry = input("enter your new entry")
                        change = mainDataBase.update_user(username,password,entry,field_choice)
                        if change:
                            print("your entry has been changed")
                        else:
                            print("your entry has not been changed")
                    case '6':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Your account have been logged out")
                        logout_flag = True
                        if logout_flag:
                            break
                    case _:
                        print("please enter a valid number from (1/2/3/4/5/6)")







if __name__ == "__main__": 
    main()

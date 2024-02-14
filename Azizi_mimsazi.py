import os
from datetime import date
import datetime

class DataBase:
    def __init__(self):
        self.users = []
        self.memes = []
        self.emails = []
        self.username = []
        self.password = []
        self.id =[]
    def log_in(self,id_number,username,password):
        if username in self.username:
            for i in range(len(self.users)):
                if self.users[i].username == username and self.users[i].password == password:
                    id_number = self.users[i].id
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"welcome {username} with id {id_number} To your account")
                    return True
        else :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("The values are invalid. Please try again.")
    def register(self,id,name,second_name,email,username,password):
        if email not in self.emails and username not in self.username:
            
                self.username.append(username)
                self.emails.append(email)
                self.users.append(Users(id,name,second_name,email,username,password))
                return True
            
    
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Username or email already exists. Please try again.")
    def create_Meme(self,meme):
        self.memes.append(meme)
    def meme_match(self,id):
        for i in range( len(self.memes)):
            if self.memes[i].id == id:
                return self.memes[i]
        return f"no meme was found with that {id}"
    def delete_meme(self,id):
        for i in self.memes:
            if i.id == id:
                self.memes.remove(i)

    def fetch_info(self, id):
        for i in self.users:
            if i.id == id:
                return i
    def update_user(self,username,password,new_entry,field):
        for i in range(len( self.users)):
            if self.users[i].username == username and self.users[i].password == password:
                if field == "username":
                    self.users[i].username = new_entry
                    self.username.remove(username)
                    self.username.append(new_entry)
                elif field == "password":
                    self.users[i].password = new_entry
    def update_meme(self, meme_name, meme_genre,meme_description,time_edit,field):
        for i in self.memes:
            if i.id == id:
                if field =="name":
                    i.name 
                    self.memes.remove(self.memes.i[1])
                if field == "genre":
                    self.meme_genre = i.genre
                    self.memes.remove(self.memes.i[2])
                if field == "description":
                    self.meme_description = print("please enter a new description:")
                    self.memes.remove(self.memes.i[3])
                
class Users:
    def __init__(self,id,name,second_name,email,username,password,):#meme_maker):
        self.id = id
        self.name = name
        self.second_name = second_name
        self.email = email
        self.username = username
        self.password = password
        #self.mememaker = "Mr.Azizi"
    def __str__(self):
        return f"Name: {self.name} {self.second_name}, Email: {self.email}, Username: {self.username}, Password: {self.password}, meme_Producer: {self.mememaker}"              
class Meme:
    def __init__(self,username, name, genre,timemake, description,id):
        self.username = username
        self.name = name
        self.genre = genre
        
        self.timemake = timemake
        self.description = description
        self.id = id
    def __str__(self):
        return f"Meme name: {self.name}, Genre: {self.genre},Max time made: {self.timemake} ,Description: {self.description}, Id: {self.id}"

        
def main():
    user_id = 0
    meme_id = 0
    dataBase = DataBase()
    success_in_login = False
    success_in_register  = False
    fragile = True
    
    while True:
        print("welcome")
        print("1.login")
        print("2.register")
        print("3.exit")
        user_enthekhab = input("Enter a number from 1 to 3: ")
        
        if user_enthekhab == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            success_in_login = dataBase.log_in(user_id,username,password) 
            
                
            
            
            
        elif user_enthekhab == "2":
            
            print(f"your account id is {user_id}")
            id = user_id
            name = input("Please type your First name: ")
            second_name = input("Please type your Last Name: ")
            user_mail = input("Please Enter your email: ")
            username = input("Please Enter your username: ")
            password = input("Please Enter your password: ")
            success_in_register = dataBase.register(id,name,second_name,user_mail,username,password)
            print(f"username {username} with id ={id} you have registered successfully .")
            if success_in_register:
                user_id += 1
                
                
        elif user_enthekhab == "3":
            print("Thank you for attending in our factory.We hope the bests for you.")
            break
        else:
            print("invalid number, please choose a number among 1/2/3:")
        
        if success_in_login:
            while True:
                print(f"Welcome to the Azizi's meme factory dear {username}!")
                print("1.Mr.Azizi Create a Meme")
                print("2.Mr.AziziNevermind(Delete Meme)")
                print("3.Show meme features")
                print("4.Show user informations")
                print("5.Edit user informations")
                print("6.Logout")
                print("7.Edit_meme")
                user_enthekhab = input("Enter your choice (1/2/3/4/5/6/7): ")
        
                
                
                if user_enthekhab == "1":
                    s=[]
                    print(f"your meme id is {meme_id}")
                    memeName = input("Enter meme name: ")
                    memeGenre = input("Enter meme genre: ")
                    memeMaxTime = datetime.datetime.now(datetime.UTC)

                    memeDescription = input("Enter meme description: ")
                    dataBase.create_Meme(Meme(username, memeName, memeGenre, memeMaxTime, memeDescription, meme_id))
                    meme_id += 1
                    print(f"{memeName} has been successfully built by {username}.")
                    
                    
                    
                elif user_enthekhab == "2":
                    id_meme_delete = input("which meme would you like to delete(id): ")
                    dataBase.delete_meme(id_meme_delete)
                    print("your meme has been sucessfully deleted")
                    
                      
                elif user_enthekhab == "3":
                    #meme_choice = int(input("Enter meme id: "))
                    #print(dataBase.meme_match(meme_choice))
                    s.append(dataBase.create_Meme(Meme(username)))
                    s.append(dataBase.create_Meme(Meme(memeName)))
                    s.append(dataBase.create_Meme(Meme(memeGenre)))
                    s.append(dataBase.create_Meme(Meme(memeMaxTime)))
                    s.append(dataBase.create_Meme(Meme(memeDescription)))
                    s.append(dataBase.create_Meme(Meme(meme_id)))
                    return s
                elif user_enthekhab == "4":
                    user_choice = int(input("enter user id:"))
                    print(dataBase.fetch_info(user_choice))
                    
                    
                    
                elif user_enthekhab == "5":
                    field_choice = input("Enter field you want to edit (username/password): ")
                    new_entry = input("Enter new value: ")
                    dataBase.update_user(username,password,new_entry,field_choice)
                        
                            
                            
                elif user_enthekhab == "6":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("you have been logedout from your account")
                    fragile = False
                    if fragile == False:
                        break
                elif user_enthekhab == "7":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You can edit your current_meme")
                    new_field = print("Enter the field you want to modify (name, genre, description): ")
                    print(dataBase.update_meme(meme_name, meme_genre,new_field))
                   
                    
                else:
                    print("invalid number, please choose a number between 1/2/3/4/5/6/7")
        
                    
               
                
main()            
                
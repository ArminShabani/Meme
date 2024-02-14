import os
from datetime import date
import datetime
class DataBase:
    def create_Meme(self,meme):
        self.memes.append(meme)
    def meme_match(self,id):
        for i in range( len(self.memes)):
            if self.memes[i].id == id:
                return self.memes[i]
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
        
    

class DataBase:
    def __init__(self):
        self.users = []
        self.usernames = []
        self.emails = []
        self.memes = []
        self.meme_names = []
    def update_user(self,username,password,new_entry,field):
        for i in self.users:
            if i.username == username and i.password == password:
                if field == "username":
                    i.username = new_entry
                    self.usernames.remove(username)
                    self.usernames.append(new_entry)
                elif field == "password":
                    i.password = new_entry
def main():
    while True:
                if choice == "6":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("you have been logedout from your account")
                    flag = False
                    if flag == False:
                        break
                else:
                    print("invalid number, please choose a number between 1/2/3/4/5/6:")
                    
main()
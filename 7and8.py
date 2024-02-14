#for the 7th part:)
class User:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.requests = []

    def add_request(self, meme_name): #ina ro haminjOori avordam ke bahal tar bashe:)
        self.requests.append(meme_name)

    def cancel_request(self, meme_name): #bar mabnaye meme_name mitOone cancel kone
        for meme in self.requests:
            if meme['name'] == meme_name:
                self.requests.remove(meme)
                return True
        return False

    def view_requests(self):
        if self.requests: #liste darkhaaste meme bar mabnaaye attribute hamOon check mishe ke bebinim darkhaasti dashte ya na
            print("Your registered requests:")
            for meme in self.requests: #baraye zamaani ke user listi az meme ro dashte bashe hame attribute ha chaap mishan
                print(f"Name: {meme['name']}, Genre: {meme['genre']}, Max Date: {meme['max_date']}, Description: {meme['description']}")
        else: #vaghti hichi az ghabl sefaaresh nadaade
            print("You have not registered any requests yet.")


def view_user_requests(user): 
    user.view_requests()



    #for the 8th part :))
class user: #baraye inke current user betOone data haye khodesh ro did bezane :)
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.requests = []

    def view_user_information(self):
        user_info = f"User Information:\n"
        user_info += f"First Name: {self.first_name}\n"
        user_info += f"Last Name: {self.last_name}\n"
        user_info += f"Email: {self.email}\n"
        user_info += f"Username: {self.username}\n"
        return user_info

''' def get_info (self):
        print(f"name is {self.first_name} {self.last_name} and your username is {self.username}")
        user1=user("kowsar","ghassemian","kowsar.ghassemian@gmail.com","kowsar011","my_hard_password")
        user1.get_info()'''
      
def display_user_information(user):
    user.view_user_information()
    
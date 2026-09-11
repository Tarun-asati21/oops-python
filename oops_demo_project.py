class chatbook :
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu() # method ko constructor ke aandar hi call kar skte hai
        
    def menu(self):
        user_input = input("""Welcome to CHATBOOK !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           -->""")
        
        if user_input == "1" :
            self.signup()
        elif user_input == "2" :
            self.signin()
        elif user_input == "3" :
            self.my_post()
        elif user_input == "4" :
            self.sendmsg()
        else :
            exit() # inbuit keyword in python to end a code
            
    def signup(self) :
        email = input("enter your email here -> ")
        pwd = input("enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu() # again called the menu function
        
    def signin(self) :
        if self.username=="" and self.password=="" : # ie username and pwd are still not defined 
            print("Please signup first by pressing 1 in the main menu")
        else :
            uname = input("enter your email/username here -> ")
            pwd = input("enter your password here -> ")
            # validate that the information entered is correct or not
            if self.username == uname and self.password == pwd :
                print("You have signed in successfully !!")
                self.loggedin = True
            else :
                print("Please input correct credentials")
                
        print("\n")
        self.menu()
        
    def my_post(self) :
        # just checking that the given user has signin done, then only is getting access to write the post otherwise not
        if self.loggedin == True :
            txt = input("Enter your message here -> ")
            print(f"following content has been posted to your CHATBOOK account -> {txt}")
        else :
            print("you need to signin first to post something...")
            
        print("\n")
        self.menu()
            
    def sendmsg(self) :
        if self.loggedin==True :
            txt = input("enter your message here -> ")
            frnd = input("whom to send the msg ?")
            print(f"your message has been sent to {frnd}")
        else :
            print("you need to signin first to post something...")
            
        print("\n")
        self.menu()
        
obj = chatbook()
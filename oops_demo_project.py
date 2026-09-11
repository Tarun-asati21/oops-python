class chatbook :
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu() # method ko constructor ke aandar hi call kar skte hai
        
    def menu(self):
        user_input = input("""
                           Welcome to CHATBOOK !! How would you like to proceed?
                           
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           """)
        
        if user_input == "1" :
            self.signup()
        elif user_input == "2" :
            self.signin()
        elif user_input == "3" :
            pass
        elif user_input == "4" :
            pass
        else :
            exit()
            
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
        
        
obj = chatbook()
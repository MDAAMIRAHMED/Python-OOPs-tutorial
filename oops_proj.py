class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to ChatBook!! How would you like to proceed
                press 1 to signup
                press 2 to signin
                press 3 to write a post
                press 4 to message a friend
                press anyother key to exit
                           
                Enter the key: """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        print()
        email = input("Enter your email here -> ")
        password = input("Enter your password here -> ")
        self.username = email
        self.password = password
        print("You have signedup successfully !!\n")
        self.menu()

    def signin(self):
        print()
        if self.username=='' and self.password == '':
            print("Please signup first !!\n")
        else:
            uname = input("Enter your email/username here -> ")
            pwd = input("Enter your password here -> ")
            if uname == self.username and pwd == self.password:
                print("You have logged in successfully !!\n")
                self.loggedin = True
            else:
                print("Invalid username or password !!\n")
        self.menu()



obj = chatbook()

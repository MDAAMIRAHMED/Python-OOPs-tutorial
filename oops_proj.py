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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

obj = chatbook()

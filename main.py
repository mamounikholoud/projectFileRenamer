from FileRenamer import File  


USER_DATA_FILE = "users1.txt"

usernames = []
passwords = []

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                usernames.append(username)
                passwords.append(password)
    except FileNotFoundError:
        pass

def save_user(username, password):
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{password}\n")

def sign_up():
    username = input("\033[33m" + "Enter a username: "+"\033[0m").strip()
    if username in usernames:
        print("\033[31m"+ "Username already taken. Please try another."+"\033[0m")
        return
    
    password = input("\033[33m"+ "Enter a password: "+"\033[0m").strip()
    usernames.append(username)
    passwords.append(password)
    save_user(username, password)  
    
    print( "Sign-up successful! You can now log in.")

def login():
    username = input("\033[33m"+ "Enter your username: "+"\033[0m").strip()
    if username not in usernames:
        print("Username not found. Please sign up first.")
        return
    
    password = input("\033[33m"+ "Enter your password: "+"\033[0m").strip()
    user_index = usernames.index(username)
    
    if passwords[user_index] == password:
        print(f"Login successful! Welcome, {username}.")
        File.FileRenamer() 
    else:
        print("Incorrect password. Please try again.")

if __name__ == "__main__":
    load_users() 
    
    while True:
        print("\033[32m"+ "\n--------------------- Menu ---------------------")
        print(      "1. Sign Up",       "2. Login",           "3. Quit")
    
        
        choice = input("\033[33m"+ "Choose an option: "+"\033[0m").strip()
        
        if choice == "1":
            sign_up()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\033[31m"+"Goodbye!"+"\033[0m")
            break
        else:
            print("Invalid option. Please try again.")
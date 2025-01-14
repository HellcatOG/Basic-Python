#initialize
username = 'admin'
password = 'secure123'
max_attempt = 3


while max_attempt > 0:
    input_username = input("Enter the username: ")
    input_password = input("Enter your password: ")

    if input_username == username and input_password == password:
        print("login Successfull")
        break
    else:
        max_attempt -= 1
        print(f"Incorrect password or username, attempts remaining: {max_attempt}")
    
else:
    print("You have 0 attempts left, Access deined")

import re

def check_username(username = None):

    username = input("Enter username:")

    if(len(username) == 0):
        print("\033[1;31;40m[Incorrect username]\033[0;37;40m\n")
        return 0
    elif(username.find(" ") > 0):
        print("\033[1;31;40m[Incorrect username]\033[0;37;40m\n")
        return 0
    else:
        print("\033[1;32;40m[Correct username]\033[0;37;40m\n")
        return 1

def check_password(password = None):

    password = input("Enter password:")

    number_pattern = "[0-9].*"
    letter_pattern = "[a-zA-Z]"
    special_character_pattern = "[^a-zA-Z0-9.]"

    if(len(password) < 8):
        return 0
    elif(
        re.search(number_pattern, password) and
        re.search(letter_pattern, password) and
        re.search(special_character_pattern, password)
    ):
        print("\033[1;32;40m[Correct password]\033[0;37;40m\n")
        return 1
    else:
        print("\033[1;31;40m[Incorrect password]\033[0;37;40m\n")
        return 0

def check_email(email = None):

    email = input("Enter email:")

    if(email.find("@") >= 0 and email.find(".") >= 0):
        print("\033[1;32;40m[Correct email]\033[0;37;40m\n")
        return 1
    else:
        print("\033[1;31;40m[Incorrect email]\033[0;37;40m\n")
        return 0


if __name__ == "__main__":
  
    check_username()
    check_email()
    check_password()
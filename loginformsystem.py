import time

print("===== This is Login System =====")

container = {
    "user": "Digvijay",
    "pass": "1234"
}

user_name = input("Enter your name: ")
user_pass = input("Enter password: ")

if user_name == container["user"] and user_pass == container["pass"]:

    time.sleep(2)
    print("Login Successful! Welcome", user_name)

else:
    time.sleep(2)
    print("Sorry! Wrong username or password.")
from cryptography.fernet import Fernet

# for initialization of key.key file
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


# write_key()


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print(f"Name: {name} , Password: {fer.decrypt(password.encode()).decode()}")


def add():
    name = input("Please enter your account name: ")
    password = input("Please enter the password for this account: ")

    with open("password.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(password.encode()).decode()}\n")


while True:
    mode = input(
        "Would you like to add a new entry('add'), view your passwords('view') or quit('Q')? "
    ).lower()

    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Please enter a valid option.")
        continue

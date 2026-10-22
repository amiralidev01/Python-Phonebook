import os

PATH = "C:/Users/Amir/Desktop/phonebook/database.txt"

if not os.path.exists(PATH):
    f = open(PATH, "w+")
    f.write("")
# Functions


def add(name, number):
    f = open(PATH, "a+")
    newPhone = name + ":" + number + "\n"
    f.write(newPhone)
    f.close()
    os.system("cls")
    print("Add Successfully")


def search(name):
    f = open(PATH, "r")
    found = False
    for line in f.readlines():
        if name == line.split(":")[0]:
            print(name + ":" + line.split(":")[1])
            found = True
            break

    f.close()

    if not found:
        print("Not Found!")


def delete(name):
    f = open(PATH, "r")
    newDatabase = ""
    for line in f.readlines():
        if not name == line.split(":")[0]:
            newDatabase += line

    f.close()

    f = open(PATH, "w")
    f.write(newDatabase)
    f.close()


def showAll():
    f = open(PATH, "r")
    docs = f.read()
    print(docs)
    f.close()


# Menu

ch = 1
while ch != 0:
    print("=============================Phone Book=============================")
    print("1-Add\n2-Search\n3-Delete\n4-Show\n0-Exit")

    ch = int(input("Enter your Choice :"))

    if ch == 1:
        name = input("Enter Name : ")
        number = input("Enter Phone Number :")
        add(name, number)
    elif ch == 2:
        name = input("Enter Name for search : ")
        search(name)
    elif ch == 3:
        name = input("Enter Name for delete : ")
        delete(name)
    elif ch == 4:
        showAll()

import datetime
import time
import os

now = datetime.datetime.now()

pins = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']
user = input("Please enter a pin: ")

if user in pins:
    print("Valid Pin")
    now = str(now)
    file = open("Valicodes.csv", "a")
    file.write(user + " " + now +"\n")
    time.sleep(2)
    os.startfile(r'C:\Users\collinpatterson\PycharmProjects\ResInIT\open.py')
elif user.__len__() > 4:
    print("Invalid Pin")
elif user not in pins:
    print("Invalid Pin")

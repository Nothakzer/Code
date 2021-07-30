# -*- coding: utf-8 -*-
storage = []
boxone = ("Box#1")
boxtwo = ("Box#2")
boxthree = ("Box#3")

number = int(input("What box are you putting into the storage system (1, 2, 3 or 123(all))?: "))
print (number)
if number == 1:
    storage.append(boxone)
if number == 2:
    storage.append(boxtwo)
if number == 3:
    storage.append(boxthree);
if number == 123:
    storage.append(boxone)
    storage.append(boxtwo)
    storage.append(boxthree)

again = input("See the storage system? (yes or no): ").lower()
print (again)  

if again == "yes": 
    print ("The storage system currently has:", (storage))
else:
    print("Bye!") ;


name = input("What is your name? ")
print(f"Hi there {name}")
howru = int(input("On a scale of 1 to 10, 1 being not so good and 10 being fantastic, how are you feeling today? "))
if howru <= 6:
    print("I'm sorry for that")
elif howru == 10:
    print("Thats amazing to hear!")
elif howru >=5 and howru <= 10:
    print("Thats nice to hear")
else:
    print("Thats not between 1 and 10")
print()
print()
age = int(input(f"So {name}, how old are you?"))
if age <= 10:
    print("Your a young user!")
elif age >= 20:
    print("Your not so young")
else:
    print("Your in the middle of being young and not so young!")
print()
print()
print("Be in mind, this program is just created for fun. Please don't go and make it harmful. That is all I have to say. Thank you for using this python program!")

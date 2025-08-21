import random 

target = random.randint(1,100)
print(target)

while True:
    userChoice = int(input("Guess the target or Quit(Q): "))
    if(userChoice == "Q" or "q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success: Correct Guess!!")
        break

    elif (userChoice < target):
        print("Your number was too small.Take a bigger guess...")
    else:
        print("Your number was too big.Take a smaller guess...")

    
print("__________Game over_______________")
    
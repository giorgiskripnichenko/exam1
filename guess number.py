
# გამოიცანი რიცხვი

import random
step = 0
userInput = None
maxNumber = 100
compNumber = random.randrange(0,maxNumber)
while userInput != compNumber:
    print()
    try:
        userInput = int(input("შეიყვანეთ რიცხვი max=100 \n"))
        step += 1
        if userInput > compNumber:
            print('მაღალია')
        else:
            print('დაბალია')
    except:
        print("wrong input")
print(f"თქვენ გამოიცანით რიცხვი {step} ჯერზე")


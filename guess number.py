
# გამოიცანი რიცხვი

import random
step = 0
userInput = None
compNumber = random.randrange(0,50)
while userInput != compNumber:
    print()
    userInput = int(input("შეიყვანეთ რიცხვი \n"))
    step += 1
    if userInput > compNumber:
        print('მაღალია')
    else:
        print('დაბალია')
print(f"თქვენ გამოიცანით რიცხვი {step} ჯერზე")


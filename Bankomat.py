
#Bankomat

import os
fileAddress = 'account.txt'
if os.path.isfile(fileAddress) == False:
    file = open(fileAddress, "w")
    file.close()

class Account:
    def __init__(self):
        pass
    def deposit(self,amount):
        with open (fileAddress,'a') as f:
            f.write(f'deposit-{amount}\n')
            f.close
        pass
    def expense(self,amount):
        with open (fileAddress,'a') as f:
            f.write(f'expense-{amount}\n')
            f.close
        pass
    def balance(self):
        stream = open(fileAddress,'rt')
        lines = stream.readlines()
        balance = 0
        for item in lines:
            if (item[0:7]) == 'deposit':
                balance += int(item[8::])
            if (item[0:7]) == 'expense':
                balance -= int(item[8::])
        result = 'ბალანსი ანგარიშზე' + str(balance)
        return(print(result))
        
account = Account()

while True:
    print('#####################################################')
    a = int(input(f'''აირჩიე ციფრი:
                  1:'ანგარიშზე შეტანა'
                  2:'ანგარიშიდან გატანა'
                  3:'ბალანსის ნახვა',
                  0:'გამოსვლა',
                   \n'''))
    if a == 1:
        try:
            amount = int(input("""შეიყვანეთ შესატანი თანხა   \n """))
            account.deposit(amount)
        except:
            print('არასწორი მონაცემების შეყვანა')

    if a == 2:
        try:
            amount = int(input("""შეიყვანეთ გამოსატანი თანხა   \n """))
            account.expense(amount)
        except:
            print('არასწორი მონაცემების შეყვანა')

    if a == 3:
        account.balance()

    if a == 0:
        exit()





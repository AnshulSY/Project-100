class atm:
    def __init__(self, cardNumber, PIN):
        self.cardNumber = cardNumber
        self.PIN = PIN
    
    def checkBalance(self):
        print("Your balance is " + str(self.cardNumber))

    def withdrawal(self, amount):
        newAmount = 50000 - amount
        print("Your withdrawal is " + str(newAmount))

def main():
    card1 = int(input("Enter your card number"))
    PIN1 = int(input("Enter your PIN"))

    p1 = atm(card1, PIN1)
    p1.checkBalance()
    p1.withdrawal(20000)

if __name__ == "__main__":
    main()


class Queue:

    def __init__(self):
        self.balance = 0
        print("Hello, Welcome to Banking Cash Counter!")

    # function for deposit
    def enqueue_deposit(self):
        amount = float(input("Enter amount to be Deposit : "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    # function for withdraw
    def dequeue_withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nWithdraw Amount does not Exist your Account ")

    # function for display
    def display(self):
        print("\nCurrent Available Balance is: ", self.balance)


# main function
if __name__ == '__main__':
    queue = Queue()
    while True:
        option = int(input("Please,select valid number from below for the action:\n1.Deposit \n2.withdraw \n"
                           "3.Display\n4.Cancel Transaction\n"))
        if option == 1:
            queue.enqueue_deposit()
        if option == 2:
            queue.dequeue_withdraw()
        if option == 3:
            queue.display()
        if option == 4:
            break

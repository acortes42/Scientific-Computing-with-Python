
class Category:

    all_category = []

    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.ledger = []  
        Category.all_category.append(self.name)

    def __str__(self):
        my_string = ""
        my_string = self.name.center(30, "*")
        if self.ledger != []:
            for x in self.ledger:
                big_desc = x['description'][:23]
                big_amount = str("{:.2f}".format(x['amount']))[:7]
                x = "{0:<23}{1:>7}".format(big_desc, big_amount)
                my_string = f"{my_string}\n{x}"
        return f"{my_string}\nTotal: " + str(round(self.amount, 2) ) + "\n"


    def deposit(self, amount, description = ""):
            self.amount += amount
            self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if (self.check_funds(amount) == True):
                self.amount -= amount
                self.ledger.append({"amount": amount, "description": description})
                return True
        return False

    def get_balance(self):
        return (self.amount)

    def transfer(self, amount, other):
        if (self.check_funds(amount) == True):
            self.withdraw(amount, "Transfer to " + other.name)
            other.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    
    def check_funds(self, amount):
        if self.amount >= amount:
            return True
        return False

def create_spend_chart(Category):

    msg = "Percentage spent by category\n"
    num_of_category = len(Category)
    percentages = []
    total_amount = 0
    all_words_complete = 0

    for i in range(num_of_category):
        total_amount += Category[i].amount
    for i in range(num_of_category):
        tmp = (int)(Category[i].amount / total_amount * 100)
        percentages.append(tmp)
    decajump = 100
    while decajump >= 0 :
        msg += str("{:>3}".format(decajump) + "|")
        for i in range(num_of_category) :
            msg += " "
            if percentages[i] >= decajump :
                msg += "o"
            else :
                msg += " "
            msg += " "
        decajump -= 10
        msg += "\n"
    msg += "    " + ("-" * num_of_category * 3) + "\n"
    for i in range(20):
        msg += " " * 5
        for num in range(num_of_category):
            if len(Category[num].name) > i:
                msg += Category[num].name[i] + " " * 2
            else:
                all_words_complete += 1
                msg += " " * 3
        if all_words_complete == num_of_category :
            break
        msg += "\n"
        all_words_complete = 0

    msg = msg[:-(num_of_category * 6)]
    print(percentages)
    return msg


def main():

    food = Category("Food")
    food.deposit(900, "deposit")
    food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
    print(food.ledger[1])
    expected = {"amount": -45.67, "description": "milk, cereal, eggs, bacon, bread"}
    return 1



if __name__ == "__main__":
    main()
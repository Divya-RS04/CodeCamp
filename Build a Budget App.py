class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*') + '\n'

        items = ''
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance()}"

        return title + items + total


def create_spend_chart(categories):
    title = 'Percentage spent by category\n'

    withdrawals = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = []
    for amount in withdrawals:
        percent = int((amount / total_spent) * 10) * 10
        percentages.append(percent)

    chart = title

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + '| '

        for percent in percentages:
            if percent >= i:
                chart += 'o  '
            else:
                chart += '   '

        chart += '\n'

    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    names = []
    for category in categories:
        names.append(category.name)

    max_length = max(len(name) for name in names)

    for i in range(max_length):
        chart += '     '

        for name in names:
            if i < len(name):
                chart += name[i] + '  '
            else:
                chart += '   '

        if i != max_length - 1:
            chart += '\n'

    return chart
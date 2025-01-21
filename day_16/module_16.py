import statistics
from collections import Counter

# Level 1: Statistics Class for Statistical Calculations
class Statistics:
    def __init__(self, data):
        self.data = sorted(data)
    
    # Method to calculate the count of data
    def count(self):
        return len(self.data)
    
    # Method to calculate the sum of data
    def sum(self):
        return sum(self.data)
    
    # Method to calculate the min value
    def min(self):
        return min(self.data)
    
    # Method to calculate the max value
    def max(self):
        return max(self.data)
    
    # Method to calculate the range (max - min)
    def range(self):
        return self.max() - self.min()
    
    # Method to calculate the mean (average)
    def mean(self):
        return statistics.mean(self.data)
    
    # Method to calculate the median
    def median(self):
        return statistics.median(self.data)
    
    # Method to calculate the mode (returns a dictionary with mode and its count)
    def mode(self):
        mode_result = statistics.multimode(self.data)
        mode_count = {num: self.data.count(num) for num in mode_result}
        return mode_count
    
    # Method to calculate the standard deviation
    def std(self):
        return statistics.stdev(self.data)
    
    # Method to calculate the variance
    def var(self):
        return statistics.variance(self.data)
    
    # Method to calculate frequency distribution (percentage frequency)
    def freq_dist(self):
        total = len(self.data)
        freq = Counter(self.data)
        return [(round(freq[key] / total * 100, 1), key) for key in freq]
    
    # Method to describe all the statistics at once
    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': self.var(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist()
        }


# Level 2: PersonAccount Class for Managing Income and Expenses
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}
    
    # Method to add an income
    def add_income(self, amount, description):
        self.incomes[description] = amount
    
    # Method to add an expense
    def add_expense(self, amount, description):
        self.expenses[description] = amount
    
    # Method to calculate the total income
    def total_income(self):
        return sum(self.incomes.values())
    
    # Method to calculate the total expense
    def total_expense(self):
        return sum(self.expenses.values())
    
    # Method to calculate the account balance (income - expenses)
    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    # Method to return account information
    def account_info(self):
        return f'Account of {self.firstname} {self.lastname}: Income = {self.total_income()}, Expenses = {self.total_expense()}, Balance = {self.account_balance()}'

# Testing the classes
if __name__ == "__main__":
    # Testing Statistics class
    ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
    data = Statistics(ages)
    
    print("Statistics for the dataset:")
    print("Count:", data.count()) 
    print("Sum:", data.sum()) 
    print("Min:", data.min()) 
    print("Max:", data.max()) 
    print("Range:", data.range()) 
    print("Mean:", data.mean()) 
    print("Median:", data.median()) 
    print("Mode:", data.mode()) 
    print("Standard Deviation:", data.std()) 
    print("Variance:", data.var()) 
    print("Frequency Distribution:", data.freq_dist()) 
    print("Description:", data.describe())

    # Testing PersonAccount class
    person = PersonAccount("John", "Doe")
    person.add_income(2000, "Job")
    person.add_income(500, "Freelance")
    person.add_expense(150, "Groceries")
    person.add_expense(100, "Utilities")
    
    print("\nPerson Account Info:")
    print(person.account_info())

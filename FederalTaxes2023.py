# 2023FederalTaxes.py
""" contains SingleFiler class and MarriedFilingJointly class """

class SingleFiler():
    """ docstring """
    def __init__(self):
        self.income = 0.0
        self.tax_rate = 0.0
        self.tax_bracket = []
        self.tax_owed = 0.0

    def set_income(self, income):
        """ docstring """
        self.income = income
        if income < 10276:
            self.tax_rate = 0.10
            self.tax_bracket.append(0)
            self.tax_bracket.append(10275)
            self.tax_owed = self.income * self.tax_rate

    def get_income(self):
        """ docstring """
        return self.income
    

class MarriedFilingJointly():
    """ docstring """
    def __init__(self):
        self.income = 0.0
        self.tax_rate = 0.0
        self.tax_bracket = []
        self.tax_owed = 0.0

    def set_income(self, income):
        """ docstring """
        self.income = income

    def get_income(self):
        """ docstring """
        return self.income

class MarriedFilingSeparately():
    """ docstring """
    def __init__(self):
        self.income = 0.0
        self.tax_rate = 0.0
        self.tax_bracket = []
        self.tax_owed = 0.0

    def set_income(self, income):
        """ docstring """
        self.income = income

    def get_income(self):
        """ docstring """
        return self.income

class HeadOfHousehold():
    """ docstring """
    def __init__(self):
        self.income = 0.0
        self.tax_rate = 0.0
        self.tax_bracket = []
        self.tax_owed = 0.0

    def set_income(self, income):
        """ docstring """
        self.income = income

    def get_income(self):
        """ docstring """
        return self.income

def switch(filing_status, income):
    """ docstring """
    if filing_status == "1":
        status = SingleFiler()
        status.set_income(income)
        return status
    if filing_status == "2":
        status = MarriedFilingJointly()
        status.set_income(income)
        return status
    if filing_status == "3":
        status = MarriedFilingSeparately()
        status.set_income(income)
        return status
    if filing_status == "4":
        status = HeadOfHousehold()
        status.set_income(income)
        return status
    #else:
    return "Invalid Entry"


def main():
    """ main function """
    income = input("How much gross income did you make in the 2023 tax year? ")
    income = income.strip("$").strip(" ").strip(",").strip(".")
    income = float(income.replace(",",""))
    print("How are you filing this year?")
    statuses = ["Single Filer", "Married Filing Jointly", "Married Filing Separately", "Head of Household"]
    filing_status = input(f"Enter 1 for {statuses[0]}, 2 for {statuses[1]}, 3 for {statuses[2]}, or 4 for {statuses[3]}: ")

    my_taxes = switch(filing_status, income)
    print(type(my_taxes))

if __name__ == "__main__":
    main()

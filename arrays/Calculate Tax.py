"""
Write a program to calculate tax if Salary and Tax Brackets are given as list in the form [ [10000, .3],[20000, .2], [30000, .1], [None, .1]]. You don’t know in the beginning how many tax brackets are there. You have to test for all of them

"""

def tax(salary, brackets):
    brackets = [[a, b] if a is not None else [0,b] for a, b in brackets] # None --> 0
    sorted_bracket = sorted(brackets, reverse=True) # Now we have the highest salary bracket first
    total_tax = 0
    for bracket, tax in sorted_bracket:
        if salary > bracket:
            total_tax += (salary - bracket)*tax
            salary -= bracket
    return total_tax
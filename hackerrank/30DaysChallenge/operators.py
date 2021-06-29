import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent = tip_percent/100 * meal_cost
    tax_percent = tax_percent/100 * meal_cost
    total_tip = tip_percent + tax_percent
    print (round(meal_cost + total_tip))
    return solve

#Test Cases(meal=12.0,tip=20,tax=8)
meal_cost = (float(input("enter meal cost: ").split.strip()))
tip_percent = int(input().strip())
tax_percent = int(input().strip())
print(solve(meal_cost,tip_percent,tax_percent))


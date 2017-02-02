# Problem 4. Write a program that calculates a 20% tip for a
# given dollar amount.
#
# Prompt the user to enter an amount. Take the input, calculate
# the tip and print out the inputed amount, tip and new total.
# Use the following format:
#
#      Amount: $10.00 Tip: $2.00 Total: $12.00
#
# You should validate the user input to ensure that the
# calculation can be completed.  If not, print a message
# to the user and end the program.
#
# The program flow should resemeble the following:
#
#   % python problem4.py
#   Enter a dollar amount? one hundred dollars
#   I was unable to calculate the tip.
#
#   % python problem4.py
#   Enter a dollar amount? 100.00
#   Amount: $100.00 Tip: $20.00 Total: $120.00
#

def tip_calculator(amount):
    tip = amount*0.2
    total = tip + amount
    print "Amount: $%.2f Tip: $%.2f Total: $%.2f" %(amount, tip, total)


amount_str = raw_input("Enter a dollar amount? ")
try:
    amount = float(amount_str)
    tip_calculator(amount)

except:
    print "I was unable to calculate the tip."

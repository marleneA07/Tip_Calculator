#Calculates how much to tip per person

bill = input('How much was the bill? $')
tip = input ("What percentage would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#(bill/people)   $100/4 = $25 each 
#(tip% + 100) / 100 = (12% + 100) / 100 = 1.12
#(bill/people) * (tip% + 100) / 100
# $25 * 1.12 = $28 each including tip
each = float(bill) / int(people)
total_tip = (int(tip) + 100) / 100
total = each * total_tip
roundTotal = round(total,2)
print(f'Each person should pay: ${roundTotal}')

#print(f'Each pearson should pay {total}') 
#format(math.pi, '.2f') 

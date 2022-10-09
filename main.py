#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill? £"))
total_people = int(input("How many people to split the bill?"))
tip_percent = float(input("What percentage tip would you like to give?"))


total_tip_amount = total_bill * (tip_percent/100)
new_total_bill = total_bill + total_tip_amount
individual_total = new_total_bill / total_people
individual_total = format(individual_total,'.2f')
print(f"The total to pay each is £{individual_total}")
# Project: tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to the tip calculator!')

# take an input of the total bill, number of persons to split the bill and the percenatge of tip
bill = float(input('what is the total bill? '))
number_of_people = int(input('how many persons should split the bill? '))
tip = float(input('how many percent tip do you want to give? 10,20,etc? '))

# divide the tip by 100 and multiply the result and the total bill
percent_tip = tip / 100
tip_to_pay = bill * percent_tip

# add the bill and tip to get the total bill and convert to 2 significant figure
total_bill = bill + tip_to_pay
total_bill_2f = "{:.2f}".format(total_bill)

# calculte the amount each person is to pay by diviidng the total bill by the number of people and covert to 2 sig fig
each_to_pay = total_bill / number_of_people
each_to_pay_2f = "{:.2f}".format(each_to_pay)

# print the result
print(f'Your total bill plus tip:  ${total_bill_2f}')
print(f'Each person is to pay: ${each_to_pay_2f}')
print('Thanks for using the calculator')
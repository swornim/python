print("welcome to the top calculator\n")
bill = float(input("what was the total bill? "))
no_p = float(input("How many people to split the bill?"))
per = float(input("what percentage topwould you like to give?"))
t_per = bill + per/100 * bill
pay = (t_per)
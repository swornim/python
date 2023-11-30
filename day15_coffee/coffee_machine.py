'''
TODO:

what would you like?(espresso/latte/cappucino):

    1) Print report.
        when the user enters "report" to prompt, a report should be generated that shows
        the current resouce values. e.g,
        water: 100ml
        milk: 50ml
        coffee: 76g
        money: $2.5


    2)check resources sufficent?
        enough resouce to make the desired coffee


    3)process coins
        quaters = $0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01

        calculate in dollar


    4)check transaction sucessful?  
        -check if resources were enough or not
        -check if user has inserted enough money to purchase the drink they selected
          and refund the money.

    5)make coffee

'''
from menu import menu,resources

#all global variables
money = 0

def print_report():
    for key in resources:
        if key == 'coffee':
            print(f"{key}: {resources[key]}g")
        else:
            print(f"{key}: {resources[key]}ml")
    print(f"money: ${money}")


def ask_coins():
    sum = 0
    print("please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    sum = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(f'total paid = {sum}')
    return sum


def make_coffee(coffee):
    global money
    check = reduce_resource(coffee)
    if check != 'insufficient':
        paid_money = ask_coins()
        return_money = 0
        if paid_money < menu[coffee]['cost']:
            print('insufficent amount, heres your return')
        else:

            return_money = paid_money - menu[coffee]['cost']
            money += (paid_money-return_money)
            print(f"here is ${return_money} in change.")
            print(f"here is your{coffee} Enjoy!")
    else:
        print("sorry! we dont have sufficient material")


def reduce_resource(coffee):
    for key in menu[coffee]['ingredients']:
        if resources[key] >= menu[coffee]['ingredients'][key]:
            if key in resources:
                resources[key] = resources[key]-menu[coffee]['ingredients'][key]
        else:
            return 'insufficient'
            
not_exit = True
while not_exit:
    coffee = input("what would you like?(espresso/latte/capppucino) or report: ").lower()

    #print report
    if coffee == 'report':
        print_report()
    elif coffee == 'exit':
        print("thank you for you time!! ")
        not_exit = False
    else:
        make_coffee(coffee)


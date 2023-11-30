from menu import menu,resources

a = menu['espresso']['cost']
coffee = 'espresso'
def reduce_resource():
    for key in menu[coffee]['ingredients']:
            if key in resources:
                resources[key] = resources[key]-menu[coffee]['ingredients'][key]
                

reduce_resource()
print(resources)
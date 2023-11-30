from prettytable import PrettyTable

table = PrettyTable() # pascal case for class
table.add_column("Pokemon",["pikachu","raichu","squirtle"])
table.add_column("type",["electric","electric",'water'])
table.align = 'l'
print(table.align)
print(table)
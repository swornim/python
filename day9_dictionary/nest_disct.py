travel_log = [
    {
        "country":"france",
        "visits":12,
        "cities":['paris','lille','dijon']
    },
    {
        "country":"germany",
        "visits":5,
        "cites":["berlin","hamburg","stuttgart"]
    },
]
print(travel_log)
def add_new_country(country_visited,number_of_times,cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = number_of_times
    new_country["cities"] = cities_visited    
    
    travel_log.append(new_country)

add_new_country("russia",2,["moscow","saint peter"])
print(travel_log)
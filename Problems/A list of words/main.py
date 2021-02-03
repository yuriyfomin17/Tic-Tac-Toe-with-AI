# work with the preset variable `words`

# new_list = [x for x in words if x[0] == "a" or x[0] == "A"]
# print(new_list)

country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
                ["New York", "Dallas", "San Francisco"]]

long_cities = []
for country in country_list:
    for city in country:
        if len(city) >= 6:
            long_cities.append(city)

print(long_cities)
print([city for country in country_list for city in country])

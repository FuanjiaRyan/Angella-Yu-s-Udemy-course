# programming_dictionary = {
#     "Bug": "An error in a program",
#     "Function": "A piece of code that can be easily called over and over again",
#     }

# # print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again"
# # print(programming_dictionary)

# empty_dictionary = {}

# # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)

# # loop through a dictionary
# for  key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested list

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# # print Lille
# print(travel_log["France"][1])

# nested_list = ["a", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])
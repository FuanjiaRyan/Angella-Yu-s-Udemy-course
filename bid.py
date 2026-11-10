programming_dictionary = {
    "Bug": "An error in a program",
    "Function": "A piece of code that can be easily called over and over again",
    }

# print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# loop through a dictionary
for  key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
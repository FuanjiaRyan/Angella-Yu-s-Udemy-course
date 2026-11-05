import random
# states = ["Delaware", "Pennysylvenis", "Texas", "Maryland"]

# states[1] = "Pencil"

# # states.append("Arizona")
# states.extend(["Ryanland", "Puzoland", "Jamesland"])


# print(states)

friends = ["Paul", "James", "Aqua", "Peter"]

# 1 Option
print(random.choice(friends))

# 2 Option
random_index = random.randint(0, 3)
print(friends[random_index])
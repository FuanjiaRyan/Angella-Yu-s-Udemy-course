# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

student_scores = [158, 56, 278, 112, 118, 123, 189, 40, 20, 50, 185, 245]

# sum = 0

# for score in student_scores:
#     sum += score

# print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
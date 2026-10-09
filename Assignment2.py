
print("What is your name?")
name = input()

print("What is your surname?")
surname = input()

print("Enter your birth year:")
year = input()

print("What about your favorite programming language?")
language = input()

age = 2026 - int(year)

adult = age >= 18

print("Name:", name.upper(), "Surname:", surname.upper(), "Age:", age, "Language:", language.upper(), "Adult:", adult, sep=" | ")

print("Enter your test score (maximum 20 points):")
score = int(input())

final_score = score // 2

print("Your final score:", final_score)
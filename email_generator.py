
name = input("Enter your name: ")
surname = input("Enter your last name: ")
platform = input("Choose a platform (gmail.com, itstep.ge, yahoo.com): ")

name = name.strip().lower()
surname = surname.strip().lower()
platform = platform.strip().lower()

name_part = name[:2]

email = f"Your email address is: {name_part}{surname}@{platform}"

print(email, end="\n\n")
print("Your email has been created successfully!")

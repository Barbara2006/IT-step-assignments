
import re

ticket_price = 15

user_input = input("შეიყვანეთ ჯავშნის ინფორმაცია: ")

try:
    numbers = re.findall(r"\d+(?:\.\d+)?", user_input)

    ticket_count = int(numbers[0])
    paid_amount = float(numbers[1])

    total_price = ticket_count * ticket_price

    if ticket_count <= 0:
        raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1")

    if paid_amount < total_price:
        raise ValueError("თანხა არ არის საკმარისი")

except IndexError:
    print("შეცდომა: ტექსტში ვერ მოიძებნა ბილეთების რაოდენობა ან გადახდილი თანხა.")

except ValueError as error:
    print(f"შეცდომა: {error}")

else:
    change = paid_amount - total_price

    print("\nჯავშნის დეტალები")
    print(f"ბილეთების რაოდენობა: {ticket_count}")
    print(f"ერთი ბილეთის ფასი: {ticket_price:.2f} ლარი")
    print(f"ჯამური ღირებულება: {total_price:.2f} ლარი")
    print(f"გადახდილი თანხა: {paid_amount:.2f} ლარი")
    print(f"დასაბრუნებელი ხურდა: {change:.2f} ლარი")
    print("ჯავშანი წარმატებით შესრულდა!")

finally:
    print("[სისტემა]: ტრანზაქციის მცდელობა დასრულდა.")

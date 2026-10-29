
#ვხსნით ფუნქციას, ფუნქციის არგუმენტი -n

def factorial_recursive(n):
   #ვამოწმებთ ცვლადი ნაკლებია თუ არა ნულზე ვინაიდან ფაქტორიალი გამოიყენება მხოლოდ დადებით რიცხვებზე
   if n < 0:
       return "Factorial is not defined for negative numbers."
   #თუ ცვლადი ტოლია 1-ის ან 0-ის, მისი ფაქტორიალი ყოველთვის უდრის ერთს, ამიტომ ფუნქციამაც უნდა გამოიტანოს 1. 
   #ეს if დებულება არის საბაზისო შემთხვევა
   if n == 0 or n == 1:
    return 1
   #თუ ცვლადი არის დადებითი და ერთზე მეტი მაშინ ვიყენებთ რეკურსიას, რისი მეშვეობითაც საწყისი ცვლადის გამოყენებით ვიკვლევთ მის წინა რიცხვს. 
   #როგორც მოცემულია, return-ში გამოყენებულია უკვე არსებული ფაკტორიალის ფუნქცია. ეს კოდს საშუალებას აძლევს რომ გაიგოს ყველა ის რიცხვი რომელიც
   #მოცემულ ცვლადამდე მოდის.
   #შესაბამისად კოდის გატარების დროს ფუნქცია n-დან 1-მდე პოულობს ყველა რიცხვს,სანამ არ მივა საბაზისო შემთხვევამდე. შემდეგ ფუნქცია 1-ს ამრავლებს 2-ზე, შემდეგ 2-ს სამზე, იმახსოვრებს თითო გამრავლების შედეგს და საბოლოოდ ამრავლებს
   #საწყის ცვლად n-ზე. ამის შედეგად ეს ფუნქცია პოულობს რიცხვის ფაქტორიალს.
   return n * factorial_recursive(n - 1)


def calculate_cart_total(discount_rate, *prices):
    total = 0
    for price in prices:
    
        discounted_price = price * (1 - discount_rate / 100)
        total += discounted_price
    return float(total)

def filter_and_sort_products(**products):

    product_list = list(products.items())
    filtered_products = filter(
        lambda item: item[1] >= 100,
        product_list
    )

    sorted_products = sorted(
        filtered_products,
        key=lambda item: item[1]
    )

    return sorted_products


print("Cart total:")
print(calculate_cart_total(10, 100, 200, 50))


print("Filtered and sorted products:")
print(filter_and_sort_products(
    laptop=2500,
    mouse=50,
    keyboard=150,
    monitor=800
))

from functools import reduce

def pair_students(names_list, scores_list):
    
    paired_data = list(zip(names_list, scores_list))

    return paired_data

def get_passed_students(paired_data, passing_score=60):

    passed_students = list(filter(
        lambda student: student[1] >= passing_score,
        paired_data
    ))

    return passed_students

def calculate_average_of_passed(passed_students):

    scores_only = list(map(
        lambda student: student[1],
        passed_students
    ))

    if len(scores_only) == 0:
        return 0.0

    total_score = reduce(
        lambda total, score: total + score,
        scores_only,
        0
    )

    average = total_score / len(scores_only)

    return average



names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]
scores = [45, 82, 91, 38, 74]

paired_data = pair_students(names, scores)
print("Paired students:")
print(paired_data)

passed_students = get_passed_students(paired_data)
print("Passed students:")
print(passed_students)

average = calculate_average_of_passed(passed_students)
print("Average score of passed students:")
print(round(average, 2))


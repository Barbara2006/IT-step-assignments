
cart_total = int(input("კალათის ღირებულება ლარებში: "))
user_status = input("მიუთითეთ: regular, vip ან admin: ").strip().lower()
has_promo_code = input("გაქვთ აქტიური პრომოკოდი (True/False): ").strip().lower() == "true"
loyalty_points = int(input("მომხმარებლის დაგროვილი ქულები: "))
delivery_city = input("ქალაქი, სადაც იგზავნება შეკვეთა: ").strip()
is_account_active = input("არის თუ არა ანგარიში აქტიური (True/False): ").strip().lower() == "true"

# Account and cart validation
if not is_account_active:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება.")
elif cart_total <= 0:
    print("კალათა ცარიელია ან მისი ღირებულება არასწორია.")
elif user_status not in ["regular", "vip", "admin"]:
    print("მომხმარებლის სტატუსი არასწორია.")
else:
    # Discount system
    discount_percent = 0

    if user_status == "vip":
        if loyalty_points >= 500:
            discount_percent = 25
        else:
            discount_percent = 20
    elif user_status == "regular" and (has_promo_code or cart_total >= 150):
        discount_percent = 10
    elif user_status == "admin":
        discount_percent = 50

    # Calculate discounted price
    discount_price = cart_total - (cart_total * discount_percent / 100)

    # Delivery fee
    if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
        if discount_price >= 100:
            delivery_charge = 0
        else:
            delivery_charge = 5
    else:
        delivery_charge = 15

    # Final invoice
    final_invoice = f"კალათის საწყისი ფასი: {cart_total} ლარი.\nფასდაკლება: {discount_percent}%.\nმიტანის საფასური: {delivery_charge} ლარი.\nსაბოლოო გადასახდელი: {discount_price + delivery_charge} ლარი."

    print("თქვენი ინვოისი:\n", final_invoice)

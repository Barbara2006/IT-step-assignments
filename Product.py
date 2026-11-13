
class Product:

    store_name = "TechShop Georgia"
    currency = "GEL"
    total_products = 0

    def __init__(self, name, price, stock, category, discount=0):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.discount = discount

        Product.total_products += 1

    def get_info(self):
        return (
            f"Name: {self.name}, "
            f"Price: {self.price} {Product.currency}, "
            f"Stock: {self.stock}, "
            f"Category: {self.category}, "
            f"Discount: {self.discount}%"
        )

    def apply_discount(self, percent):
        self.discount = percent
        print(f"Discount for {self.name} updated to {percent}%")

    def update_stock(self, amount):
        if self.stock + amount < 0:
            print("Warning: Insufficient stock!")
        else:
            self.stock += amount
            print(f"New stock for {self.name}: {self.stock}")

    def calculate_final_price(self):
        return self.price - (self.price * self.discount / 100)

    @classmethod
    def get_total_products_count(cls):
        return cls.total_products

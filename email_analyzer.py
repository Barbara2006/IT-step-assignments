
import re

text = "ჩვენი გუნდის წევრები არიან: saba.ananidze@itstep.com, მეგობარი დიმა dima123@gmail.com და კიდევ ერთი ტესტური მისამართი test_user@yahoo.com"

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

result = "+".join(emails)

print(result)

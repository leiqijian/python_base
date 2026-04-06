import re

mobile = input("phone :")
# result = re.search('^1[2-9]\d{9}$', mobile)
result = re.match(r"itcast\d", "itcast5")
if result:
    print(result.group())
else:
    print("false")
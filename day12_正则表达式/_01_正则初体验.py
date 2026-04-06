import re

result = re.match('abc', 'abd')

if result:
    print(result.group())
else:
    print("不满足条件")
import re

text = '문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다.'
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)
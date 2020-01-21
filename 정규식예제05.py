import re
 
text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
 
regex = re.compile(r'(?P<area>\d{3})-(?P<num>\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group("area")
num = matchobj.group("num")
print(areaCode, num) 
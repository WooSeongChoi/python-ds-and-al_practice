import re

text = '에러 1122 : 레퍼런스 오류\n 에러 1033 : 아규먼트 오류'
regex = re.compile('에러\s\d+')
mc = regex.findall(text)
print(mc)
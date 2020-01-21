import re

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)

"""
정규 표현식은 단순한 리터럴 문자열을 검색하는 것보다 훨씬 많은 기능들을
제공하는데, 즉, 특정 패턴의 문자열을 검색하는데 매우 유용하다.
그 한가지 예로 웹페이지나 텍스트에 특정 패턴의 전화번호를 발췌하는
기능이 있다고 가정하자.
정규식에서는 숫자를 의미하는 기호로 \d를 사용한다.
여기서 d는 digit를 의미하고 0-9까지의 숫자중 아무거나 될 수 있다.
따라서, 위 전화번호 패턴을 정규식으로 표현하면
\d\d\d-\d\d\d-\d\d\d\d 와 같이 될 수 있다.
"""
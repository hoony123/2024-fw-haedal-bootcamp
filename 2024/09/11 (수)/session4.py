'''weather = "맑음"

if weather == "비" : #1
	print("우산을 챙기세요.")
elif weather == "미세먼지" : #2
	print("마스크를 챙기세요.")
else:
	print("준비물이 필요 없어요.")'''

'''w=input('오늘의 날씨는 어때요?')
if w == "비" : #1
	print("우산을 챙기세요.")
elif w == "미세먼지" : #2
	print("마스크를 챙기세요.")
else:
	print("준비물이 필요 없어요.")
	
def open_account():
	print("새로운 계좌를 개설합니다.")'''
	
def withdraw(balance, money) :
	print("{0}원을 출금했습니다. 잔액은 {1}원 입니다.".format(money,(balance-money)))
	return balance - money
balance = 0
balance = withdraw(balance, 1000)

def profile(name, age, *languages):
	print("이름 : {0}\t나이 : {1}\t".format(name, age), end =" ")
	for lang in languages:
		print(lang, end=" ")
	print()

profile("찰리", 20, "파이썬", "자바", "C", "C++", "C#")   
profile("루시", 25, "코틀린", "스위프트") 
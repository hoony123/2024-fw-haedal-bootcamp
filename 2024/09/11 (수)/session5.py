'''class Unit:
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5)
soldier2 = Unit("보병", 40, 5)
tank = Unit("탱크", 150, 35)



try : 
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("오류 발생! 잘못된 값을 입력했습니다.")'''

'''class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, damage):
        try :
            self.health -= damage
            if self.health <= 0:
                raise ValueEroor("Game Over")
            print()'''
class Person:
    # 클래스 변수 선언
    species = '사람'

    # 인스턴스 메서드
    # 인스턴스가 활용할 메서드
    def greeting(self):
        print('안녕하세요~!')

iu = Person()
iu.greeting() # ()는 메서드 호출

#클래스 변수(속성)
print(Person.species)
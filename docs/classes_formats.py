# class 사용 순서
# 1. import : 같은 파일에 있을 경우 생략
# 2. class instance
# 3. call function

# class basic format
class Class_name:
    def __init__(self) :      # 생성자
        pass

    def function_name(self) :     # self 키워드 필요(class 소속 확인용)
        pass
        return 0

#예제
class Person:
    def add_age(self) : 
        pass
        print("45세")
        return 0
# 1. import : 같은 파일에 있을 경우 생략
## 같은 파일에 있으니 생략
# 2. class instance
## 다음에 사용하기 위해 변수에 담기
person = Person()
# 3. call function
## 호출할때 규칙(.class_name())
person.add_age()

#예제
# 4칙연산 되는 class 작성
# 덧셈, 뺄셈
class Arithmetics:
    def __init__(self) :      # 생성자(class 갖고 있는 자원)
        pass

    def add(self, first, second) :
        sum = first + second
        return sum  # 상수 대신 변수 사용

    def minus(self, first, second) :
        result = first - second
        return 0
    
# 1. import : 같은 파일에 있을 경우 생략
##같은 파일에 있으니 생략
# 2. class instance : 생성자 호출
## 다음에 사용하기 위해 변수에 담기
arithmetics = Arithmetics()
# 3. call function : 원하는 기능 호출
arithmetics.add(5, 6)

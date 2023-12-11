# 덧셈, 뺄셈, 곱셈, 나눗셈
class Arithmetics:
    def __init__(self) :      # 생성자(class 갖고 있는 자원)
        pass

    def add(self, first, second) :                  ####예외처리 하세요!!!!!!
        result = first + second
        return result

    def minus(self, first, second) :
        result = first - second
        return result
    
    def multiplication(self, first, second) :
        result = first * second
        return result
    
    def division(self, first, second) :
        result = first / second
        return result
    
# 1. import : 같은 파일에 있을 경우 생략
##같은 파일에 있으니 생략
# 2. class instance : 생성자 호출
## 다음에 사용하기 위해 변수에 담기
arithmetics = Arithmetics()
# 3. call function : 원하는 기능 호출


print(arithmetics.add(5, 6))
print(arithmetics.minus(5, 6))
print(arithmetics.multiplication(5, 6))
print(arithmetics.division(5, 6))
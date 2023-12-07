# 기본 function 형식 - 기다림, 불리울 때 기능한다.
def function_name() :
  pass          #내용 넣기
  return 0      #return할 내용 넣기(return은 값만 나옴)

## 그냥 연습
def my_function():
  print("Hello from a function")

## function 부르기
my_function()
pass

# 문항 1과 답항을 출력하는 function
def print_question_and_answer() :
    str_anyone = "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
    print(str_anyone)
    str_anyone = "A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
    print(str_anyone)

    return 0

# print_question_and_answer()

## 나오는 값 처리

def add() :
    num_first = 5
    num_second = 4
    sum = num_first + num_second
    return sum  # 상수 대신 변수 사용

# num_sum = 0
num_sum = add()      # 2차, 3차 활용을 위해서 해당하는 값을 어떠한 변수에다가 담아서 활용
print("add() return 결과 : {}".format(num_sum)
print(add())

def minus() :
    first = 5
    second = 4
    total = first - second
    return total
num_total = minus()
print("minus() returm 결과 : {}".format(num_total))

#예제
def multiply() :
    num_1st = 4
    num_2nd = 5
    result = num_1st * num_2nd
    return result
num_result = multiply()
print("multiply() 의 결과 : {}".format(num_result))




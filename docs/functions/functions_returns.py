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

## call by reference
## 나오는 값 처리

def add() :
    num_first = 5
    num_second = 4
    sum = num_first + num_second
    return sum  # 상수 대신 변수 사용

# num_sum = 0
num_sum = add()      # 2차, 3차 활용을 위해서 해당하는 값을 어떠한 변수에다가 담아서 활용
print("add() return 결과 : {}".format(num_sum))
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


print("--------------------")

#예제
def return_list() :     
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits
print("return_list() return result : {}".format(return_list()))

# list 중에 index로 값 return
def return_listbyindex() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits[0] 
print("return_listbyindex() return resul: {}".format(return_listbyindex()))

print("----------------------")

# 반복적인 print 작업을 줄이기 위한 function 만들기
def score() :
    my_score = 79
    my_grade = ''
    if my_score >= 90 :
        my_grade = 'A'
    elif my_score > 80 :
        my_grade = 'B'
    else :
        my_grade = 'C'
    return my_grade
str_grade = return_grade()
print("당신의 학점은 {}입니다.".format(str_grade))
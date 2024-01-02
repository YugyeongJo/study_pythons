# def multiply() :
#     num_1st = 4
#     num_2nd = 5
#     result = num_1st * num_2nd
#     return result
# num_result = multiply()
# print("multiply() 의 결과 : {}".format(num_result))

# def score() :
#     my_score = 79
#     my_grade = ''
#     if my_score >= 90 :
#         my_grade = 'A'
#     elif my_score > 80 :
#         my_grade = 'B'
#     else :
#         my_grade = 'C'
#     return my_grade
# str_grade = score()
# print("당신의 학점은 {}입니다.".format(str_grade))

def calculator():
    while True :
        str_input_multiply = "곱셈을 희망하는 수를 입력해주세요 : "
        multiply01 = input("{}".format(str_input_multiply))
        multiply02 = input("{}".format(str_input_multiply))
        if multiply01 == "q" or multiply02 == "q":
            break
        else : 
            num_multiply01 = int(multiply01)
            num_multiply02 = int(multiply02)
        result = num_multiply01 * num_multiply02
        print("결과는 {} 입니다.".format(result))
    return 0
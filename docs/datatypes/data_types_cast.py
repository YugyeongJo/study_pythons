# pass
type("yugyeongjo") # 문자 type
# <class 'str'>

type(1997) # 숫자 type
# <class 'int'> 

name = "yugyeongjo"   # 문자 type
type(name)
# <class 'str'>

age = 24 # 숫자 type
type(age)
# <class 'int'>

# 터미널 입력 값에 대한 증명
str_input = input("문자 입력 : ")
print("입력({}) type 표시 : {}".format(str_input, type(str_input)))
num_input = input("숫자 입력 : ")
print("입력({}) type 표시 : {}".format(num_input, type(num_input)))
# teminal로 들어온 값은 모두 str 문자로 인식
pass
# cast : data type 변경
# int(num_input)
# 1997
# type(int(num_input))
# <class 'int'>

# cast 불가 경우
# 숫자가 아닌 것이 섞여있는 경우 casting이 안됨.
# mix_val = "23k"
# int(mix_val)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '23k'
pass
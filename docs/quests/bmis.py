str_input_weight = "몸무게 : "
num_input_weight = input("{}".format(str_input_weight))

str_input_height = "키 : "
num_input_height = input("{}".format(str_input_height))

int_weight = int(num_input_weight) 
int_height = int(num_input_height)/100

num_bmi = int_weight / (int_height ** 2)
str_bmi = "BMI :"
answer = print("{} {}".format(str_bmi,num_bmi))

if num_bmi >= 25 :          
    print("{}점은 25점 이상이기 때문에 비만입니다.".format(num_bmi))
elif num_bmi >= 23 :       
    print("{}점은 23점 이상이기 때문에 과체중입니다.".format(num_bmi))
elif num_bmi >= 18 :       
    print("{}점은 18점 이상이기 때문에 정상입니다.".format(num_bmi))
else :         
    print("{}점은 18점 미만이기 때문에 저체중입니다.".format(num_bmi))
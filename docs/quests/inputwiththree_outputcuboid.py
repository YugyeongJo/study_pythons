#  - 가로 * 세로 * 높이 = 직육면체 부피
#  - input : 가로 세로 높이
#  - output : 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3

str_input_width = "가로 : "
num_input_width = input("{}".format(str_input_width))

str_input_depth = "세로 : "
num_input_depth = input("{}".format(str_input_depth))

str_input_height = "높이 : "
num_input_height = input("{}".format(str_input_height))

int_width = int(num_input_width)
int_depth = int(num_input_depth)
int_height = int(num_input_height)

num_volume = int_width*int_depth*int_height

str_volume = "정육면체 부피 :"
answer = print("{} {}".format(str_volume,num_volume))

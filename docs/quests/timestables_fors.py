# quest 3 구구단 5단 for문 사용

times = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for five_times in times:
    pass
    print("5 * {} = {}".format(five_times, 5*five_times))

    

# quest 4 구구단 for문 사용
# - 단 수 입력받아서 사용

times = [1, 2, 3, 4, 5, 6, 7, 8, 9]

str_howmany_times = "몇단? "
num_howmany_times = int(input("{}".format(str_howmany_times)))

for five_times in times:
    pass
    print("{} * {} = {}".format(num_howmany_times, five_times, num_howmany_times*five_times))
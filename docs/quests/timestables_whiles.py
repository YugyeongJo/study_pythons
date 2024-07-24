#quest multiplication table
# - 구구단 5단 단계별 표시

five_times_table = 0

while five_times_table < 9 :
    five_times_table = five_times_table + 1

    num_five_times_table = 5 * five_times_table

    print("5 * {} = {}".format(five_times_table, num_five_times_table))


#quest2 multiplication table
# - 단을 입력받아 구구단 단계별 표시

what_times_table = "가로 : "
num_at_times_table = input("{}".format(what_times_table))


times_table = 0

while times_table < 9 :
    times_table = times_table + 1

    num_table = what_times_table * times_table
    # print(table)

    print("{} * {} = {}".format(what_times_table, times_table, num_table))
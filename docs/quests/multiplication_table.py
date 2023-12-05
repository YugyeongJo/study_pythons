#quest multiplication table
# - 구구단 5단 단계별 표시

five_times_table = 0

while five_times_table < 9 :
    five_times_table = five_times_table + 1

    num_five_times_table = 5 * five_times_table

    print("5 * {} = {}".format(five_times_table, num_five_times_table))
# - [30, 35, 20] 단 대한 출력
# - timestables_fors.py -> function 화
# - option) [30, 35, 20] 부분 사용자 입력, 'q'이면 종료

def calculator ():
    while True :
        times = input("몇 단을 출력하시겠습니까?")
        
        if times == "q":
            break    
        
        num_times = int(times)
        
        count = [0,1,2,3,4,5,6,7,8]
        for i in count:
            multiply = num_times * (count[i]+1)
            print("{}*{}={}".format(num_times, (count[i]+1), multiply))
    return 0

calculator ()
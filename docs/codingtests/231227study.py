a,b,c = map(int, input("숫자 3개를 각각 입력하세요 : ").split())
play = int(input("도전횟수를 입력하세요 : "))
# d,e,f = map(int, input("도전할 숫자 3개를 각각 입력하세요 : ").split())

strike = 0
ball = 0

for i in range(play):
    d,e,f = map(int, input("도전할 숫자 3개를 각각 입력하세요 : ").split())
    strike = 0
    ball = 0
    for x in range(1): 
        if a==d : 
            strike += 1
        elif b==e : 
            strike += 1
        elif c==f :
            strike += 1
        else : 
            strike = strike
            pass
        
        if d == (b or c) : 
            ball += 1
        elif e == (a or c) :
            ball += 1
        elif f == (a or b) : 
            ball += 1
        else : 
            ball = ball
        
    result = "{}S {}B".format(strike, ball)
    if result == "0S 0B":
        print("아웃")
    else :
        print(result)
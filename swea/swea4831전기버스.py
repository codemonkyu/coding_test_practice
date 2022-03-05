T = int(input())
for test_case in range(1, T + 1):
    #K: 이동 가능한 거리, N: 종점, M: 충전소 개수
    K, N, M = map(int, input().split(" "))
    #stations: 충전 가능 정류장 정보
    stations= list(map(int, input().split(" ")))
    
    #1
    now = 0
    can_go = now+K
    charge_station = 0
    count = 0
    
    #2
    while (can_go<N):
        #3
        for i in stations:
            if now < i <= can_go:
                charge_station = i
            elif can_go < i:
                break
        #4
        if charge_station == -1:
            count = 0
            break
        #5
        now = charge_station
        can_go = now+K
        count += 1
        charge_station = -1
        
    print(f"#{test_case} {count}")
    
    
    #다시풀어보기
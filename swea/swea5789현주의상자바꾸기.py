T = int(input())

for tc in range(1, T+1):
    # n은 상자의 개수, q는 상자의 값을 변경할 횟수
    N, Q = map(int, input().split())
    # 값이 0인상자를 n개 만들어주자
    # 여기서 str형태로 넣어주는 이유는 출력시 join을 이용하기위해
    box = ['0']*N
    
    #q회를 반복함 여기서 변수 i는 한번 돌때마다 그 위치에 상자 값이 i임을 뜼함
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        
        for j in range(L-1, R):
            box[j] = str(i)
            
    print(f'#{tc}',' '.join(box))
    #문제의 출력에 빈칸이 있다. 빈칸을 갖고 하나씩 조인해준다.
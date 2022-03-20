test_case=int(input())

for i in range(1, test_case+1):
    N,M = map(int, input().split())
    N_list = list(map(int, input().split()))
    new_list = []
    for j in range(N-M+1):
        result=0
        for k in range(j, j+M):
            result += N_list[k]
        new_list.append(result)
        
    print(f'#{i} {max(new_list)-min(new_list)}')
for tc in range(1, int(input())+1):
    N = int(input())
    TC = list(map(int, input().split()))
    max_value = 0

    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if TC[i] > TC[j]:
                cnt += 1

        if cnt > max_value:
            max_value = cnt

    print(f'#{tc} {max_value}')
T = int(input())

for x in range(1, T+1):

    N = int(input())
    ai = list(map(int, input().split()))

    max = ai[0]
    min = ai[0]
    for num in ai:
        if max < num:
            max = num
        if num < min:
            min = num
    
    result = max - min
    
    print(f'#{x} {result}')
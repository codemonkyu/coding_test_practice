for tc in range(1, 11):
    dump = int(input())
    data = list(map(int, input().split()))
    box = [0 for i in range(0, 101)]
    
    minValue = 100
    maxValue = 1
    
    for i in range(0, 100):
        box[data[i]] += 1 
        if data[i] > maxValue:
            maxValue = data[i]
            
        if data[i] < minValue:
            minValue = data[i]
            
    while dump > 0 and minValue < (maxValue -1):
        box[minValue] -= 1
        box[minValue + 1] += 1
        
        box[maxValue] -= 1
        box[maxValue -1] += 1
        
        if box[minValue] == 0:
            minValue += 1
            
        if box[maxValue] == 0:
            maxValue -= 1;
            
        dump -= 1
        
    print(f'#{tc} {maxValue - minValue}')
    
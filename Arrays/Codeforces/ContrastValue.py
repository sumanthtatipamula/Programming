for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split()))
    result = 0
    right = 1
    inc, dec = None, None
    while(right < len(elements)):
        if(elements[right - 1] < elements[right]):
            result += 2 if(not inc and not dec) else 1
            inc = True
            while(right < len(elements) and elements[right - 1] <= elements[right]):
                right += 1
            if(right < len(elements) and elements[right - 1] > elements[right]):
                result += 1
                while(right < len(elements) and elements[right - 1] >= elements[right]):
                    right += 1   
        elif(elements[right - 1] > elements[right]):
            result += 2 if(not inc and not dec) else 1
            dec = True
            while(right < len(elements) and elements[right - 1] >= elements[right]):
                right += 1
            if(right < len(elements) and elements[right - 1] < elements[right]):
                result += 1
                while(right < len(elements) and elements[right - 1] <= elements[right]):
                    right += 1
        else:
            while(right < len(elements) and elements[right - 1] == elements[right]):
                right += 1

    print(1 if(result == 0) else result)
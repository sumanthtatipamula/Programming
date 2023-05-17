for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split()))
    result, max_value = 0, elements[0]
    for i in range(1, len(elements)):
        if(elements[i] > 0 and elements[i - 1] < 0 or elements[i] < 0 and elements[i - 1] > 0):
            result += max_value
            max_value = elements[i]
        else:
            max_value  = max(elements[i], max_value)
    print(result + max_value)
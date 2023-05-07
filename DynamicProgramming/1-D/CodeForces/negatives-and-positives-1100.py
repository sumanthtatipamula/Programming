for _ in range(int(input())):
    n = int(input())
    elements = list(map(int, input().split()))
    min_element = float("Inf")
    count, total = 0, 0
    for element in elements:
        min_element = min(min_element, abs(element))
        total += abs(element)
        if(element < 0):
            count += 1
    if(count % 2 != 0):
        total -= 2 * min_element
    print(total)
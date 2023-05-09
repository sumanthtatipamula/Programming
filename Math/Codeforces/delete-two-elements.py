for _ in range(int(input())):
    n = int(input())
    elements = list(map(int,input().split()))
    total = sum(elements)
    freq = defaultdict(int)
    for element in elements:
        freq[element] += 1
    need = 2 * (total) // n
    if(2 * (total) % n != 0):
        print(0)
        continue;
    result = 0
    for element in elements:
        a1, a2 = element, need - element
        if(a1 == a2):
            result -= 1
        if(freq[a2]):
            result += freq[a2]
    print(result // 2)
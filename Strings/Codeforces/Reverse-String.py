for _ in range(int(input())):
    source, target = input(), input()
    indices = []
    for i in range(len(source)):
        if(source[i] == target[0]):
            indices.append(i)
    possible = False
    for i in indices:
        k = 0
        for j in range(i, len(source)):
            if(k == len(target)):
                possible = True
                break;
            if(target[k] != source[j]):
                break;
            else:
                k += 1
                l = k
                m = j - 1
                while(l != len(target) and m >= 0):
                    if(target[l] == source[m]):
                        l += 1
                        m -= 1
                    else:
                        break;
                if(l == len(target)):
                    possible = True
                    break;
        if(possible):
            break;

    print("NO" if(not possible) else "YES")

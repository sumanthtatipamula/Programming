from math import ceil

for _ in range(int(input())):
    n = int(input())
    r, p, s = map(int, input().split())
    bob_moves = input()
    br,bp,bs = 0,0,0
    for move in bob_moves:
        if(move == 'R'):
            bp += 1
        elif(move == 'P'):
            bs += 1
        else:
            br += 1
    loses = (abs(bp - p) + abs(bs - s) + abs(br - r)) // 2
    if(loses > int(ceil(n / 2)) or (n % 2 != 0 and loses == ceil(n / 2))):
        print("NO")
    else:
        print("YES")
        bp -= p
        bs -= s
        br -= r
        result = ""
        for move in bob_moves:
            if(move == 'R'):
                if(bp > 0 and bs < 0):
                    bp -= 1
                    bs += 1
                    result += 'S'
                elif(bp > 0 and br < 0):
                    bp -= 1
                    br += 1
                    result += 'R'
                else:
                    result += 'P'
            elif(move == 'S'):
                if(br > 0 and bp < 0):
                    br -= 1
                    bp += 1
                    result += 'P'
                elif(br > 0 and bs < 0):
                    br -= 1
                    bs += 1
                    result += 'S'
                else:
                    result += 'R'
            else:
                if(bs > 0 and bp < 0):
                    bs -= 1
                    bp += 1
                    result += 'P'
                elif(bs > 0 and br < 0):
                    bs -= 1
                    br += 1
                    result += 'R'
                else:
                    result += 'S'
        print(result)
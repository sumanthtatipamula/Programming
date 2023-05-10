for _ in range(int(input())):
    s, t = input(), input()
    if(len(s) <= len(t)):
        if(s != t):
            print("NO")
        else:
            print("YES")
        continue
    s_index, t_index = len(s) - 1, len(t) - 1
    while(t_index > -1 and s_index > -1):
        if(s[s_index] == t[t_index]):
            s_index  -= 1
            t_index -= 1
        else:
            s_index -= 2
    print("YES" if(t_index < 0) else "NO")
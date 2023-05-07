for _ in range(int(input())):
    string, target, count = input(), "codeforces", 0
    for i in range(10):
        if(string[i] != target[i]):
            count += 1
    print(count)
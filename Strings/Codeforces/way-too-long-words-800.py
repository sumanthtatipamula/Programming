for _ in range(int(input())):
    string = input()
    if(len(string) <= 10):
        print(string)
        continue;
    print(string[0] + str(len(string) - 2) + string[-1])
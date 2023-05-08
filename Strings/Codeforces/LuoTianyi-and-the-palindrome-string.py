# def find_max_length(left, right, string):
#     max_length = 0
#     while(left > -1 and right < len(string)):
#         if(string[left] != string[right]):
#             max_length = max(max_length, right - left + 1)
#         elif(string[left] != string[right - 1] or string[left + 1] != string[right]):
#             max_length = max(max_length, right - left)
#         left -= 1
#         right += 1
#     return max_length

# for _ in range(int(input())):
#     string = input()
#     reversed_string = string[::-1]
#     if(string != reversed_string):
#         print(len(string))
#     max_length = 0
#     for i in range(0, len(string)):
#         max_length = max(max_length, find_max_length(i - 1, i + 1, string))
#     print(max_length if(max_length) else -1)

for _ in range(int(input())):
    string = input()
    reversed_string = string[::-1]
    if(string != reversed_string):
        print(len(string))
    max_length = 0
    isNonSubsequence = False
    for i in range(0, len(string)):
        if(string[i] != string[0]):
            isNonSubsequence = True
            break;
    print(-1 if(not isNonSubsequence) else len(string) - 1)

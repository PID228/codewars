def solution(s):
    a_list = []
    r = s if len(s) % 2 == 0 else f'{s}_'
    for i in range(0, len(r), 2):
        a_list.append(r[i:i + 2])

    return a_list


print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))

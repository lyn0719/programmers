# 문제: 프로그래머스 120893 - 대문자와 소문자
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    my_string = list(my_string)
    
    for i in range(len(my_string)):
        if my_string[i].islower():
            my_string[i] = my_string[i].upper()
        else:
            my_string[i] = my_string[i].lower()
    
    answer = ''.join(my_string)
    return answer
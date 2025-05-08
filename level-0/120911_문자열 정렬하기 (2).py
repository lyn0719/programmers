# 문제: 프로그래머스 120811 - 문자열 정렬하기 (2)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(my_string):
    answer = ''
    
    my_string = my_string.lower()
    my_string = ''.join(sorted(my_string))
    
    answer = my_string
    return answer
# 문제: 프로그래머스 181907 - 문자열의 앞의 n글자
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181907

def solution(my_string, n):
    answer = ''
    
    answer = my_string[:n]
    return answer
# 문제: 프로그래머스 12912 - 두 정수 사이의 합
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    
    if a ==  b:
        return a
    if a > b:
        a, b = b, a
    
    for i in range(a, b+1):
        answer += i
    return answer
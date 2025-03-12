# 문제: 프로그래머스 120837 - 개미 군단
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    answer = 0
    
    a = hp // 5
    b = (hp % 5) // 3
    c = ((hp % 5) % 3) // 1
    
    answer = a + b + c
    
    return answer
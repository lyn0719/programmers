# 문제: 프로그래머스 120891 - 369게임
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    
    order = str(order)
    
    for char in order:
        if char in "369":
            answer += 1
    
    return answer
# 문제: 프로그래머스 120810 - 세균 증식
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120810

def solution(n, t):
    
    answer = n
    
    for i in range(t):
        answer *= 2
        
    return answer
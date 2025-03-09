# 문제: 프로그래머스 120813 - 짝수는 싫어요
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = []
    
    a = 1
    
    for a in range (n+1):
        if a % 2 == 1:
            answer.append(a)
        
    return answer
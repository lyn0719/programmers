# 문제: 프로그래머스 120831 - 짝수의 합
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):   
    answer = 0
    
    for i in range(n+1):
        if(i % 2 == 0):
            answer += i
        
    return answer
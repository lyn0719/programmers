# 문제: 프로그래머스 120814 - 피자 나눠 먹기 (1)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    answer = 0
    
    if(n % 7 != 0):
        answer = (n//7) + 1
    else:
        answer = n//7
    return answer
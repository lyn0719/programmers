# 문제: 프로그래머스 120816 - 피자 나눠 먹기 (3)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    answer = 0
    
    if n % slice >= 1:
        answer = (n // slice) + 1
    else:
        answer = n // slice
    return answer
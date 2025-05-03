# 문제: 프로그래머스 120836 - 순서쌍의 개수
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    answer = 0
    cnt = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    answer = cnt
    return answer
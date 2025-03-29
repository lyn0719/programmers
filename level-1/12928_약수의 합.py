# 문제: 프로그래머스 12928 - 약수의 합
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    i = n

    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer
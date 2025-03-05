# 문제: 프로그래머스 120906 - 자릿수 더하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    answer = 0
    i=0
    n = str(n)
    for i in range(len(n)):
        answer += int(n[i])
    return answer
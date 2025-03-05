# 문제: 프로그래머스 120830 - 양꼬치
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    answer = (12000 * n) + (2000 * k) - ((n//10)*2000)
    return answer
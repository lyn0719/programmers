# 문제: 프로그래머스 181937 - n의 배수
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181937

def solution(num, n):
    answer = 0
    
    if num % n == 0:
        return 1
    else:
        return 0

# 문제: 프로그래머스 12937 - 짝수와 홀수
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    answer = ''
    
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer
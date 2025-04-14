# 문제: 프로그래머스 82612 - 부족한 금액 계산하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1
    result = 0
    
    for i in range(1, count+1):
        result += price * i
    
    answer = result - money
    
    if answer <= 0:
        return 0

    return answer
# 문제: 프로그래머스 120819 - 아이스 아메리카노
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819

def solution(money):
    answer = []
    
    num = money // 5500
    charge = money % 5500
    
    answer = [num, charge]
    return answer
# 문제: 프로그래머스 120889 - 삼각형의 완성조건 (1)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    answer = 0
    
    Max = max(sides)
    sides.remove(Max)
    num = int(sides[0] + sides[1])
    
    if Max>=num:
        answer = 2
    else:
        answer = 1
    
    return answer
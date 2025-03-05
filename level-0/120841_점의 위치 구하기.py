# 문제: 프로그래머스 120841 - 점의 위치 구하기기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    answer = 0
    
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:
        answer = 3
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    return answer
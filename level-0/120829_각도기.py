# 문제: 프로그래머스 120829 - 각도기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    if(angle<90):
        answer = 1
    elif(angle == 90):
        answer = 2
    elif(90 < angle < 180):
        answer = 3
    elif(angle == 180):
        answer = 4
    
    return answer
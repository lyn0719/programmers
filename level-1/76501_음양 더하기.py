# 문제: 프로그래머스 76501 - 음양 더하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] == True and absolutes[i] >= 0:
            answer += absolutes[i]
        else:
            answer += -(absolutes[i])
    return answer
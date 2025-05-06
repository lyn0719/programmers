# 문제: 프로그래머스 131705 - 삼총사
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    answer = 0
    cnt = 0
    
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    cnt += 1
    
    answer = cnt
    return answer
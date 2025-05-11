# 문제: 프로그래머스 136798 - 기사단원의 무기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = 0
    t_list = [0] * (number+1)
    
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            t_list[j] += 1
    
    for i in range(len(t_list)):
        if t_list[i] > limit:
            t_list[i] = power
            answer += t_list[i]
        else:
            answer += t_list[i]
    
    return answer
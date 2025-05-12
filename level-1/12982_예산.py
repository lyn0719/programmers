# 문제: 프로그래머스 12982 - 예산
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    t_sum = 0
    cnt = 0
    
    d.sort()
    
    for i in range(len(d)):
        if t_sum + d[i] <= budget:
            t_sum += d[i]
            cnt += 1
        
    answer = cnt
    return answer
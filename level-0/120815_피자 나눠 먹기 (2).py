# 문제: 프로그래머스 120815 - 피자 나눠 먹기 (2)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    answer = 0
    cnt = 6
    
    if cnt % n == 0:
        answer = 1
    else:
        while True:
            cnt += 6
            if cnt % n == 0:
                answer = cnt // 6
                break
                
    return answer
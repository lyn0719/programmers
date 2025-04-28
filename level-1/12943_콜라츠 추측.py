# 문제: 프로그래머스 12943 - 콜라츠 추측
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    cnt = 0
    
    if num == 1:
        return 0

    while num != 1:
        if num % 2 == 0:
            num //= 2
            cnt += 1
        else:
            num = num * 3 + 1
            cnt += 1
        
        if cnt >= 500:
            return -1
    
    answer = cnt
    
    return answer
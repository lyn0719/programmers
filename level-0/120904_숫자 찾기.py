# 문제: 프로그래머스 120904 - 숫자 찾기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    answer = 0
    num = list(map(int, str(num)))
    
    for i in range(len(num)):
        if k in num:
            answer = num.index(k) + 1
        else:
            answer = -1
            
    return answer
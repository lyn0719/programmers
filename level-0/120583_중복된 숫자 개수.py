# 문제: 프로그래머스 120583 - 중복된 숫자 개수
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120583

def solution(array, n):
    answer = 0
    cnt = 0
    
    for i in range(len(array)):
        if array[i] == n:
            cnt += 1
            
    answer = cnt
    return answer
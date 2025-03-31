# 문제: 프로그래머스 12944 - 평균 구하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = 0
    cnt = 0
    ssum = 0
    
    for i in range(len(arr)):
        ssum += arr[i]
        cnt += 1
    
    answer = ssum / cnt
    return answer
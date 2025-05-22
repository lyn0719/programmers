# 문제: 프로그래머스 181882 - 조건에 맞게 수열 변환하기 1
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181882

def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] = arr[i] * 2
    
    answer = arr
        
    return answer
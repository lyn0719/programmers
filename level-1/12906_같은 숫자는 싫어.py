# 문제: 프로그래머스 12906 - 같은 숫자는 싫어
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    
    return answer
# 문제: 프로그래머스 12910 - 나누어 떨어지는 숫자 배열
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            answer.sort()
    
    if len(answer) == 0:
        return [-1]
    
    return answer
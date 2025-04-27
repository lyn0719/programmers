# 문제: 프로그래머스 12935 - 제일 작은 수 제거하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        return answer
    
    a = min(arr)
    print(a)
    
    for i in range(len(arr)):
        if arr[i] != a:
            answer.append(arr[i])
    
    return answer
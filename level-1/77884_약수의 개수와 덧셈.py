# 문제: 프로그래머스 77884 - 약수의 개수와 덧셈
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
    
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer
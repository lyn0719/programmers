# 문제: 프로그래머스 12944 - 평균 구하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12944

def solution(x, n):
    answer = []
    
    
    for i in range(1, n+1):
        answer.append(x*i)
    return answer
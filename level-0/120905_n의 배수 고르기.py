# 문제: 프로그래머스 120905 - n의 배수 고르기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    answer = []
    
    for i in range(len(numlist)):
        if(numlist[i] % n == 0):
            answer.append(numlist[i])
    return answer
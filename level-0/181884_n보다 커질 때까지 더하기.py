# 문제: 프로그래머스 181884 - n보다 커질 때까지 더하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    answer = 0
    
    for i in range(len(numbers)):
        answer += numbers[i]
        if answer > n:
            return answer
    return answer
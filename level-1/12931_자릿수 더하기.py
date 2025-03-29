# 문제: 프로그래머스 12931 - 자릿수 더하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    nstr = str(n)
    
    for i in range(len(nstr)):
        answer += int(nstr[i])

    return answer
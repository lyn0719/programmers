# 문제: 프로그래머스 12922 - 수박수박수박수박수박수?
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer
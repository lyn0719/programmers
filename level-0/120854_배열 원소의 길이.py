# 문제: 프로그래머스 120854 - 배열 원소의 길이이
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    answer = []
    
    for i in range(len(strlist)):
        answer.append(len(strlist[i]))
    return answer
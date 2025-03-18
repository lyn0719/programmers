# 문제: 프로그래머스 120908 - 문자열안에 문자열
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    answer = 0
    
    for char in str1:
        if str2 not in str1:
            answer = 2
        else:
            answer = 1
    return answer
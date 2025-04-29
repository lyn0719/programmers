# 문제: 프로그래머스 12918 - 문자열 다루기 기본
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False
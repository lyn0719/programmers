# 문제: 프로그래머스 12917 - 문자열 내림차순으로 배치하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    
    a = sorted(s, reverse=True)
    
    answer = ''.join(a)

    return answer
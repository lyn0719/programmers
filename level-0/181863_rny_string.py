# 문제: 프로그래머스 181863 - rny_string
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181863

def solution(rny_string):
    answer = ''
    
    answer = rny_string.replace('m', 'rn')
    return answer
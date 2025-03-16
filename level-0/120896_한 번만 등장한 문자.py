# 문제: 프로그래머스 120896 - 한 번만 등장한 문자
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    answer = ''
    tlist = ''

    for char in s:
        if s.count(char) == 1:
            tlist += char
    
    answer = ''.join(sorted(tlist))
    return answer
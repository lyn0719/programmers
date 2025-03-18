# 문제: 프로그래머스 120849 - 모음 제거
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    alist = 'aeiou'
    
    for char in my_string:
        if char not in alist:
            answer += char
            
    return answer
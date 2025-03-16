# 문제: 프로그래머스 120888 - 중복된 문자 제거
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = ''
    
    for char in my_string:
        if char not in answer:
            answer += char
            
    return answer
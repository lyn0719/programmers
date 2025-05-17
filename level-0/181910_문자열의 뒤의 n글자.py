# 문제: 프로그래머스 181910 - 문자열의 뒤의 n글자
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181910

def solution(my_string, n):
    answer = ''
    
    answer = my_string[len(my_string)-n:]
    return answer
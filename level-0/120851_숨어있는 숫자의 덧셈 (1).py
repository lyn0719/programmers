# 문제: 프로그래머스 120851 - 숨어있는 숫자의 덧셈 (1)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    answer = 0
    
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            answer += int(my_string[i])
    return answer
# 문제: 프로그래머스 86051 - 없는 숫자 더하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = -1
    t_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s_sum = 0
    
    for i in t_list:
        if i not in numbers:
            s_sum += i
    
    answer = s_sum
    
    return answer
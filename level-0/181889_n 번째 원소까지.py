# 문제: 프로그래머스 181889 - n 번째 원소까지
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181889

def solution(num_list, n):
    answer = []
    
    answer = num_list[:n]
    return answer
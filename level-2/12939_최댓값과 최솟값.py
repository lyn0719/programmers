# 문제: 프로그래머스 12939 - 최댓값과 최솟값
# 난이도: Level 2
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    
    s_list = [int(x) for x in s.split()]
    
    s_max = max(s_list)
    s_min = min(s_list)
    
    answer = str(s_min) + ' ' + str(s_max)
    
    return answer
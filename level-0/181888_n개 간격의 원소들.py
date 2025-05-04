# 문제: 프로그래머스 181888 - n개 간격의 원소들
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181888

def solution(num_list, n):
    answer = []
    
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
        
    return answer
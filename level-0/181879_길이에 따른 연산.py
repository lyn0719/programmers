# 문제: 프로그래머스 181879 - 길이에 따른 연산
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181879

def solution(num_list):
    answer = 0
    n = 1
    
    if len(num_list) >= 11:
        for i in range(len(num_list)):
            answer += num_list[i]
    else:
        for i in range(len(num_list)):
            n *= num_list[i]
            answer = n
    return answer
# 문제: 프로그래머스 181929 - 원소들의 곱과 합
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    answer = 0
    num_sum = 0
    num_mul = 1
    
    for i in range(len(num_list)):
        num_sum += num_list[i]
        num_mul *= num_list[i]
        
    num_square = num_sum * num_sum
    
    if(num_mul >= num_square):
        return 0
    else:
        return 1

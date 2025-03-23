# 문제: 프로그래머스 120824 - 짝수 홀수 개수
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    answer = []
    count1 = 0
    count2 = 0
    
    for num in num_list:
        if num % 2 == 0:
            count1 += 1
        else:
            count2 += 1
        
    answer.append(count1)
    answer.append(count2)
    return answer
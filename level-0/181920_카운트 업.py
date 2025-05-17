# 문제: 프로그래머스 181920 - 카운트 업
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181920

def solution(start_num, end_num):
    answer = []
    
    for i in range(start_num, end_num+1, 1):
        answer.append(i)
    return answer
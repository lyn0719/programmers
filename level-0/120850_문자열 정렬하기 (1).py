# 문제: 프로그래머스 120850 - 문자열 정렬하기 (1)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            answer.append(int(my_string[i]))
            answer.sort()
    return answer
# 문제: 프로그래머스 120844 - 배열 회전시키기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    answer = []
    
    if direction == "right":
        answer = [numbers[-1]] + numbers[:-1]
    else:
        answer = numbers[1:] + [numbers[0]]

    return answer
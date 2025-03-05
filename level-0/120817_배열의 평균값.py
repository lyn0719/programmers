# 문제: 프로그래머스 120817 - 배열의 평균값
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    answer = sum(numbers)
    answer = answer/len(numbers)
    return answer
# 문제: 프로그래머스 120809 - 배열 두 배 만들기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809

def solution(numbers):
    answer = [ 2 * x for x in numbers]
    return answer
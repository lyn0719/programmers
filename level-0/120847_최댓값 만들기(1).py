# 문제: 프로그래머스 120847 - 최댓값 만들기(1)
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    answer = 0
    
    a = max(numbers)
    numbers.remove(a)
    
    b = max(numbers)
    
    answer = a * b
    return answer
# 문제: 프로그래머스 120825 - 문자 반복 출력하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''.join([i * n for i in my_string])
    return answer
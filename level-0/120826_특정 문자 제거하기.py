# 문제: 프로그래머스 120826 - 특정 문자 제거하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826

def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer
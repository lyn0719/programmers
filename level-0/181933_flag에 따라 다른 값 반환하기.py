# 문제: 프로그래머스 181933 - flag에 따라 다른 값 반환하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181933

def solution(a, b, flag):
    answer = 0
    
    if flag == True:
        return a + b
    else:
        return a - b

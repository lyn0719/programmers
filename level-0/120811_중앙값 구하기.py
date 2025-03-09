# 문제: 프로그래머스 120811 - 중앙값 구하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    answer = 0
    
    array.sort()
    
    n = (len(array) // 2)
    
    answer = array[n]
    return answer
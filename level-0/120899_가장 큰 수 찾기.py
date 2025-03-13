# 문제: 프로그래머스 120899 - 가장 큰 수 찾기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    answer = []
    
    a = max(array)
    answer.append(a)
    b = array.index(max(array))
    answer.append(b)
    
    return answer
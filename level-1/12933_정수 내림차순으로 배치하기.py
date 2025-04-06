# 문제: 프로그래머스 12933 - 정수 내림차순으로 배치하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    num = []
    
    num = list(str(n))
    
    num.sort()
    num.reverse()
    
    num = int(''.join(num))
    
    answer = num
    return answer
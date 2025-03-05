# 문제: 프로그래머스 120585 - 머쓱이보다 키 큰 사람
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    answer = 0
    
    for i in range(len(array)):
        if array[i] > height:
            answer += 1
            
    return answer
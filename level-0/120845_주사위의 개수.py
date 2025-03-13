# 문제: 프로그래머스 120845 - 주사위의 개수
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    answer = 0
    
    row = box[0] // n
    col = box[1] // n
    height = box[2] // n
    
    answer = row * col * height
    
    return answer
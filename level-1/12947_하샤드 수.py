# 문제: 프로그래머스 12947 - 하샤드 수
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    
    list_x = list(str(x))
    
    x_sum = sum([int(i) for i in list_x])
    print(x_sum)
    
    if x % x_sum == 0:
        return True
    else:
        return False
    
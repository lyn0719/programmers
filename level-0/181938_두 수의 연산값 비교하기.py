# 문제: 프로그래머스 181938 - 두 수의 연산값 비교하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181938

def solution(a, b):
    answer = 0
    
    if ( (2*a*b) > int(str(a) + str(b)) ):
        answer = 2 * a * b
    else:
        answer = int(str(a) + str(b))
    return answer
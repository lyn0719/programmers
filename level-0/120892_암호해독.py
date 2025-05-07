# 문제: 프로그래머스 120892 - 암호해독
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = ''
    
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer
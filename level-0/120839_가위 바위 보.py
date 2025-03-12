# 문제: 프로그래머스 120839 - 가위 바위 보
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answer = ''
    
    for i in range(len(rsp)):
        if rsp[i] == "2":
            answer += "0"
        elif rsp[i] == "0":
            answer += "5"
        elif rsp[i] == "5":
            answer += "2"
    
    return answer
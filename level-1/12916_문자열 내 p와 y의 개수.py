# 문제: 프로그래머스 12916 - 문자열 내 p와 y의 개수
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    p_list = ["p", "P"]
    y_list = ["y", "Y"]
    cnt_p, cnt_y = 0, 0
    
    for ch in s:
        if ch in p_list:
            cnt_p += 1
        elif ch in y_list:
            cnt_y += 1
    
    if cnt_p == cnt_y:
        return True
    else:
        return False
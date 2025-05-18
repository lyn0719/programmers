# 문제: 프로그래머스 181878 - 원하는 문자열 찾기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    answer = 0
    
    myString = myString.lower()
    pat = pat.lower()
    
    if pat not in myString:
        return 0
    else: 
        return 1

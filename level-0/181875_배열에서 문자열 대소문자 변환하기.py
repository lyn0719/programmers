# 문제: 프로그래머스 181875 - 배열에서 문자열 대소문자 변환하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181875

def solution(strArr):
    answer = []
    
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    
    answer = strArr
    return answer
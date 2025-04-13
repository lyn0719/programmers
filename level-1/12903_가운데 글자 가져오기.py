# 문제: 프로그래머스 12903 - 가운데 글자 가져오기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    
    middle = len(s) // 2
    
    if len(s) % 2 == 0:
        answer = s[middle-1 : middle+1]
    else:
        answer = s[middle]
    return answer
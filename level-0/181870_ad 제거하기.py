# 문제: 프로그래머스 181870 - ad 제거하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    answer = []
    
    for ch in range(len(strArr)):
        if "ad" not in strArr[ch]:
            answer.append(strArr[ch])
        
    return answer
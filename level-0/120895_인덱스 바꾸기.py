# 문제: 프로그래머스 120895 - 인덱스 바꾸기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895

def solution(my_string, num1, num2):
    answer = ''

    alist = list(my_string)
    
    alist[num1], alist[num2] = alist[num2], alist[num1]
    
    answer = "".join(alist)
    return answer
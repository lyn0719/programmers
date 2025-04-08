# 문제: 프로그래머스 12948 - 핸드폰 번호 가리기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    
    fn = '*' * (len(phone_number) - 4)
    
    answer = fn + phone_number[-4:]
    return answer
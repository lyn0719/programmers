# 문제: 프로그래머스 120818 - 옷가게 할인 받기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    return price
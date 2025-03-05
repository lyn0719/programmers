# 문제: 프로그래머스 120808 - 분수의 덧셈
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120808

from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    answer = [answer.numerator, answer.denominator]
    return answer
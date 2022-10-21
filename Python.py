# 프로그래머스 코딩 Test 입문

## 두 수의 합

### 1.
def solution(num1, num2):
    answer = num1 + num2
    return answer

### 2.
solution = lambda num1, num2 : num1 + num2

## 두 수의 차

### 1.
def solution(num1, num2):
    answer = num1 - num2
    return answer

### 2.
solution = lambda num1, num2 : num1 - num2

## 두 수의 곱

### 1.
def solution(num1, num2):
    answer = num1 * num2
    return answer

### 2.
solution = lambda num1, num2 : num1 * num2

## 두 수의 나눗셈

### 1.
def solution(num1, num2):
    answer = num1 / num2
    return answer

### 2.
solution = lambda num1, num2 : num1 / num2

## 몫 구하기

### 1.
def solution(num1, num2):
    answer = num1 // num2
    return answer

### 2.
solution = lambda num1, num2 : num1 // num2

## 나머지 구하기

### 1.
def solution(num1, num2):
    answer = num1 % num2
    return answer

### 2.
solution = lambda num1, num2 : num1 % num2

## 숫자 비교하기

### 1.
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

### 2.
def solution(num1, num2):
    return 1 if num1==num2 else -1

## 분수의 덧셈 -> https://dimenchoi.tistory.com/46 참조

### 1.
def solution(denum1, num1, denum2, num2):
    answer = []
    # 두 수가 배수관계일때.
    if max(num1, num2) % min(num1, num2) == 0:
        tmp =  max(num1,num2) // min(num1,num2)
        if num1 <= num2:
            answer = [denum1*tmp + denum2, num2]
        else:
            answer = [denum2*tmp + denum1, num1]
    # 두 수가 배수관계가 아닐때.
    else:
        answer = [(denum2*num1) + (denum1*num2), num1 * num2]
    
    ############# 약분을 안한 answer 출력 ##############
    
    # answer 약분되는지 판별
    div = 2 # 1로 나눠지는 것은 의미가 없기 때문에 2부터 시작
    # 분자와 분모 중 더 작은 수가 div보다 크거나 같을 때까지만 반복
    while min(answer[0], answer[1]) >= div:
        # 분자, 분모 모두 div로 나눠질 경우
        if answer[0] % div == 0 and answer[1] % div == 0: 
            answer[0] = answer[0] // div
            answer[1] = answer[1] // div
        # div로 약분이 안될 경우    
        else:
            div += 1
    return answer

### 2.
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num) # 최대공약수 구하는 함수
    return [denum//gcd, num//gcd]

### 3. https://wikidocs.net/106676 참조
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

### 4.
def solution(denum1, num1, denum2, num2):
    # 최소공배수 구하는 함수
    def lcm(a,b):
        if a % b == 0:
            return b
        else:
            return lcm(b, a % b)
        
    l = lcm((num2*denum1 + num1*denum2), num1*num2)
    return ((num2*denum1 + num1*denum2)//l , num1*num2//l)

## 배열 두배 만들기

### 1.
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(2 * num)
    return answer

### 2. https://wikidocs.net/22 참조
def solution(numbers):
    return [num * 2 for num in numbers]

### 3. https://blockdmask.tistory.com/531 참조
def solution(numbers):
    answer = list(map(lambda x : x*2, numbers))
    return answer



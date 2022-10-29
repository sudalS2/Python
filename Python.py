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
from fractions import Fraction # 유리수를 계산할 때 사용하는 모듈

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2) # Fraction(분자, 분모) 형태
    return [answer.numerator, answer.denominator] # numerator: 분자를 알 수 있음, denominator: 분모를 알 수 있음

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

## 중앙값 구하기

### 1.
import numpy as np

def solution(array):
    answer = np.median(array)
    return answer

### 2.
def solution(array):
    return sorted(array)[len(array) // 2] # 정렬 후 배열의 길이 / 2 의 몫인 순서 값 반환(배열의 카운팅은 0 부터 시작)

## 최빈값 구하기

### 1.
from collections import Counter

def solution(array):
    c = Counter(array)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for i in order:
        if i[1] == maximum:
            modes.append(i[0])
    print(modes)
    
    if len(modes) == 1:
        return modes[0]
    else:
        return -1

### 2.
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1

### 3.
from collections import Counter

def solution(array):
    a = Counter(array).most_common(2)
    if len(a) == 1:
        return a[0][0]
    if a[0][1] == a[1][1]:
        return -1
    return a[0][0]

### 4.
def solution(array):
    keys = set(array)
    dict = {}
    max_freq = []
    for key in keys:
        dict[key] = array.count(key)
    for key in keys:
        if dict[key] == max(dict.values()):
            max_freq.append(key)
    if len(max_freq) > 1:
        answer = -1
    else:
        answer = max_freq[0]
    return answer

## 짝수는 싫어요

### 1.
def solution(n: int) -> list:
    return [x for x in range(1, n+1) if x % 2 == 1]

### 2.
def solution(n):
    return [i for i in range(1, n+1, 2)]

### 3.
def solution(n):
    return [x for x in range(n + 1) if x % 2]

## 피자 나눠 먹기(1)

### 1. 
import math

def solution(n):
    answer = math.ceil(n / 7)
    return answer

### 2.
def solution(n):
    if n % 7 == 0:
        return (n // 7)
    else:
        return (n // 7) + 1
    
### 3.
def solution(n):
    return (n - 1) // 7 + 1

## 피자 나눠먹기(2)

### 1.
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1

### 2.
import math

def solution(n):
    answer = ((6 * n)/math.gcd(6, n)) // 6
    return answer

## 피자 나눠먹기(3)

### 1.
def solution(slice, n):
    answer = (n-1) // slice + 1
    return answer

### 2.
import math

def solution(slice, n):
    answer = math.ceil(n/slice)
    return answer

## 배열의 평균값

### 1.
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer

### 2.
import numpy as np

def solution(numbers):
    return np.mean(numbers)

## 옷가게 할인 받기

### 1.
def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)

### 2.
def solution(price):
    price_rates = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    for sale_price, sale_rate in price_rates.items():
        if price >= sale_price:
            return int(price * sale_rate)

### 3.
def solution(price):
    if price >= 100000 and price < 300000:
        return int(price * (1-0.05))
    if price >= 300000 and price < 500000:
        return int(price * (1-0.1))
    if price >= 500000:
        return int(price * (1-0.2))
    else:
        return price

## 아이스 아메리카노

### 1.
def solution(money):
    answer = [money//5500, money%5500]
    return answer

### 2.
def solution(money):
    return divmod(money, 5500)

## 나이 출력

### 1.
def solution(age):
    answer = 2022 - (age-1)
    return answer

## 배열 뒤집기

### 1.
def solution(num_list):
    return list(reversed(num_list))

### 2.
def solution(num_list):
    return num_list[::-1]

### 3.
def solution(num_list):
    num_list.reverse()
    return num_list

### 4.
def solution(num_list):
    answer = []
    for i in range(1,len(num_list)+1):
        answer.append(num_list[-i])

    return answer

## 각도기

### 1.
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

### 2.
def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    elif angle > 0:
        return 1
    
## 중복된 숫자 개수

### 1.
def solution(array, n):
    cnt = array.count(n)
    return cnt

### 2.
from collections import Counter

def solution(array, n):
    return Counter(array)[n]

## 문자열 뒤집기

### 1.
def solution(my_string):
    answer = my_string[::-1]
    return answer

### 2.
def solution(my_string):
    answer = ''

    for i in range(len(my_string)-1, -1, -1) :
        answer += my_string[i]
    return answer

### 3.
def solution(my_string):
    return ''.join(list(reversed(my_string)))

## 직각삼각형 출력하기

### 1.
n = int(input())

for i in range(1,n+1,1):
    print(i * '*')
    
## 짝수 홀수 개수

### 1. map(함수, 반복 가능한 자료형(튜플,리스트)) : 리스트 값들에 함수를 적용 map객체 -> list 혹은 tuple로 형 변환해줘야 함.
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]

### 2.
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

### 3.
def solution(num_list):
    a = []
    b =[]
    
    for i in num_list:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
            
    return [len(a),len(b)]

## 문자 반복 출력하기

### 1.
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

### 2.
def solution(my_string, n):
    answer = ''
    
    for i in my_string:
        answer += i * n
    return answer

## 특정 문자 제거하기

### 1.
def solution(my_string, letter):
    return my_string.replace(letter, '')

### 2.
def solution(my_string, letter):
    answer = ''    
    for i in my_string:
        if letter != i:
            answer += i
    return answer

## 양꼬치

### 1.
def solution(n, k):
    answer = (n*12000) + ((k-(n//10))*2000)
    return answer

### 2.
def solution(n, k):
    service = n//10
    drink = max(0, k-service)
    return (12000*n)+(2000*drink)

## 짝수의 합

### 1.
def solution(n):
    answer = sum(range(0,n+1,2))
    return answer

### 2.
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

## 배열 자르기

### 1.
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

## 외계행성의 나이

### 1.
def solution(age):
    return ''.join([chr(ord('a')+int(i)) for i in str(age)])

### 2.
def solution(age):
    change = ['a','b','c','d','e','f','g','h','i','j']
    age = list(str(age))
    return ''.join([change[int(i)] for i in age])

### 3. 
def solution(age):
    PG_AGE= {0:'a', 1:'b', 2:'c', 3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}
    age_list = list(map(int,str(age))) # = [int(a) for a in str(age)]
    answer= ''
    for i in range(0, len(age_list)):
        answer += PG_AGE[age_list[i]]
    return answer

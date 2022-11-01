# 해시

## 완주하지 못한 선수

### 1.
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

### 설명
counter["l"] += 1 -> 원소 카운트 1개 더하기
counter["h"] -= 1 -> 원소 카운트 1개 빼기

ex) Counter('hellow world') -> Counter({'h': 0, 'e': 1, 'l': 4, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

most_common(): 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
ex) Counter('hello world').most_common() -> [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
ex) Counter('hello world').most_common(1) -> [('l', 3)]

### 2.
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= int(hash(com))
    answer = dic[temp]

    return answer
  
  ### 3.
  def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
  
  ### 4.
  def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
  
## 폰켓몬

### 1.
import collections

def solution(nums):
    c_nums = collections.Counter(nums)
    if len(c_nums) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(c_nums)T
    
### 2.
def solution(nums):
    return min(len(set(nums)), len(nums)//2)

### 3.
def solution(nums):
    answer = 0
    myList = set(nums)
    if len(nums)/2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums)/2
    return answer

## 전화번호 목록

### 1.
def solution(phoneBook):
    phoneBook.sort()
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

### 2.
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

### 3. -> 효율성 실패
from itertools import combinations as c

def solution(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook)
    for (a,b) in c(sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer

## 4. -> 효율성 실패
def solution(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True

## 위장

### 1.

### 2.
### 3.
  
## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.


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

## 폰켓몬

### 1.
### 2.
### 3.

## 폰켓몬

### 1.
### 2.
### 3.


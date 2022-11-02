# 해시 -> 딕셔너리 데이터 이해

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

### 4. -> 효율성 실패
def solution(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True

## 위장

### 1. 
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1
    return answer

### 설명
- functools.reduce(집계 함수: lambda 식 사용 가능, [순회 가능한 데이터] : list 형식, 초기값=시작값)
ex) reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1 => 1 * (2+1) = 3 -> 3 * (1+1) = 6 -> 6 - 1 = 5

### 2.
import collections
from functools import reduce

def solution(clothes):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in clothes]).values()])-1

### 3.
def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num
        
    return cnt - 1

## 베스트앨범

### 1.
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]]) # 같은 장르에 [재생횟수, 인덱스 값] 추가
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
        
    return answer

### 설명
- list(set(genres)) -> ["classic","pop"] : 순서가 없고, 집합안에서는 unique한 값, mutable 객체

- zip(genres, plays, range(len(plays))) -> [["classic",500,0],["pop",600,1],["classic",150,2],["classic",800,3],["pop",2500,4]]
ex) dict(zip(["year", "month", "date"], [2001, 1, 31])) -> {'year': 2001, 'month': 1, 'date': 31}    
ex) numbers = ["1", "2", "3"], letters = ["A"]
    list(zip(numbers, letters)) -> [('1', 'A')] : 길이가 짧은 리스트에 맞춰서 나머지 버려짐
        
- d = {"classic":[[0,500],[2,150],[3,800]],"pop":[[1,600],[4,2500]]}      
        
### 2.
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i) # i는 인덱스 번호

    return answer

### 설명
- enumerate(): 리스트에서 요소와 인덱스 얻기
- zip(): 여러개의 리스트에서 요소들 얻기
ex) names = ['Alice', 'Bob', 'Charlie'], ages = [24, 50, 18]
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

# 0 Alice 24
# 1 Bob 50
# 2 Charlie 18    

- dic1 = {"classic":[[0,500],[2,150],[3,800]],"pop":[[1,600],[4,2500]]}
- dic2 = {"classic":1450,"pop":3100}

- sorted(dic2.items(), key=lambda x:x[1], reverse=True) : dic2를 재생수 별로 내림차순 정렬 -> [["pop",3100],["classic",1450]]
- sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2] : dic1['pop'],dic1['classic']를 재생수 별로 내림차순 정렬한 것을 앞에서 2개만 추출 
-> 'pop'일 경우 [[4,2500],[1,600]],'classic'일 경우 [[3,800],[0,500]]



### 3.
def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer


# 정렬

## K번째수

### 1.
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1]) 
    return answer

### 2.
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

### 3.
def solution(array, commands):
    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]

### 4.
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

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


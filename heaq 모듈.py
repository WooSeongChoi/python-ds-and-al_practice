import heapq
import copy

list1 = [4,6,8,1]
heapq.heapify(list1)
print(list1)

# 항목을 heap에 삽입할 때는 heapq.heappush(heap, item)을 사용한다.
h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'have fun'))
heapq.heappush(h, (3, 'work'))
heapq.heappush(h, (4, 'study'))
print(h)


# heapq.heappop(heap) 함수는 힙에서 가장 작은 항목을 제거하고 반환한다. pop
print(heapq.heappop(list1))
print(list1)


# heapq.heappushpop(heap, item)은 새 항목을 힙에 추가한 후, 가장 작은 항목을 제거하고 반환한다.
# 다른말로 하면 heapq.heappush(haep, item)하고 난 다음에 heapq.heappop(heap)을 하는 것과 같다.
heapq.heappush(list1, 1)
print(list1)
temp = list1[:]

heapq.heappush(list1, 3)
heapq.heappop(list1)
print(list1)

list1 = temp[:]
heapq.heappushpop(list1, 3)
print(list1)


# heapq.heapreplace(heap, item)은 힙의 가장 작은 항목을 제거하고 반환한 후에, 새항목을 추가한다.
# 다시말하면 heapq.heappop(heap)을 하고 heapq.heappush(heap, item)을 하는 것과 같다.
temp = list1[:]
print(heapq.heapreplace(list1, 5))
print(list1)

list1 = temp[:]
print(heapq.heappop(list1))
heapq.heappush(list1, 5)
print(list1)


# heappush()와 heappop()을 따로 사용하는 것 보다. heappushpop() heapreplace()를 사용하는 것이 더 효율적이다.
# 힙의 속성을 사용하면 많은 연산 할 수 있다.

# heapq.merge(*iterables)는 여러개의 정렬된 반복 가능학 객체를 병합하여 한나의 정렬된 결과의 이터레이터를 반환한다.
for x in heapq.merge([1,3,5],[2,4,6]):
    print(x, end = ' ')
print()

# heapq.nlargest(n, iterable[, key])와 heapq.nsmallest(n, iterable[, key])는 
# 데이터에서 n개의 가장 큰 요소와 가장 작은 요소가 있는 리스트를 반환한다.

array = list(range(10))
temp = copy.deepcopy(array)
result = heapq.nsmallest(4,array)
print (result)
result = heapq.nlargest(3,array)
print (result)

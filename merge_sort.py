def merge_sort(seq):
    # pop()을 이용한 병합 정렬
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    
    res = []
    # left와 right가 둘다 비어있지 않다면
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()

    # left가 차있으면 left, left가 비어있으면 right
    return(left or right) + res

def test_merge_sort():
    seq = [3,5,2,6,8,1,0,3,5,6,2]
    assert(merge_sort(seq) == sorted(seq))
    print('테스트 성공!')

if __name__ == '__main__':
    test_merge_sort()
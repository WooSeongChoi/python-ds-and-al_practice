def insertion_sort_rec(seq, i=None):
    if i is None:
        i = len(seq) - 1
    if i == 0:
        return i
    insertion_sort_rec(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

"""
재귀를 함으로써 for문을도는 효과를 가진다.
for문을 도는 것이 더 효과적일 듯.
"""

def test_insertion_sort_rec():
    seq = [11,3,28,43,9,4]
    assert(insertion_sort_rec(seq) == sorted(seq))
    print('테스트 성공!')

if __name__ == '__main__':
    test_insertion_sort_rec()
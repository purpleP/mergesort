from hypothesis import given
from hypothesis import strategies as st

from collections import Counter

def merge(left, right):
    # breakpoint()
    left, right = iter(left), iter(right)
    stop = object()
    r = next(right, stop)
    if r is stop:
        yield from left
        return
    while (l := next(left, stop)) is not stop:
        if l <= r:
            yield l
        else:
            yield r
            r, right, left = l, left, right
    yield r
    yield from right


@given(
    st.lists(st.integers()),
    st.lists(st.integers()),
)
def test_merge(left, right):
    left.sort()
    right.sort()
    merged = list(merge(left, right))
    assert is_sorted(merged)
    assert Counter(left + right) == Counter(merged)


def is_sorted(xs):
    return all( prev <= curr for prev, curr in zip(xs, xs[1:]))


## ```bisect```

Array bisection algorithm

```python
import bisect
```

| Method                      | Description                                     |
| :-------------------------- | :---------------------------------------------- |
| ```bisect.bisect_left(list, item[, lo[, hi]])```        | Locate the proper insertion point for item in list to maintain sorted order. The parameters lo and hi may be used to specify a subset of the list which should be considered; by default the entire list is used. If item is already present in list, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first parameter to ```list.insert()```. This assumes that list is already sorted.  |
| ```bisect.bisect_right(list, item[, lo[, hi]])```        | Similar to ```bisect_left()```, but returns an insertion point which comes after (to the right of) any existing entries of item in list.
         |
| ```bisect.bisect(...)```        | Alias for ```bisect.bisect_right(...)```        |
| ```bisect.insort_left(list, item[, lo[, hi]])```        | Insert item in list in sorted order. This is equivalent to ```list.insert(bisect.bisect_left(list, item, lo, hi), item)```. This assumes that list is already sorted.
       |
| ```bisect.insort_right(list, item[, lo[, hi]])```        | Similar to ```insort_left()```, but inserting item in list after any existing entries of item.         |
| ```bisect.insort(...)```        | Alias for ```bisect.insort_right(...)```        |




#### Bisection Algorithm Example

```python
grades = "FEDCBA"
breakpoints = [30, 44, 66, 75, 85]
from bisect import bisect
def grade(total):
    return grades[bisect(breakpoints, total)]

grade(66)
Out[]:
'C'

map(grade, [33, 99, 77, 44, 12, 88])

Out[]:
['E', 'A', 'B', 'D', 'F', 'A']
```

```python
import bisect
def binary_search(A, B):
    clip = lambda idx: max(min(len(A) - 1, idx), 0)
    C = []
    for b in B:
        idx = bisect.bisect(A, b)
        # A[idx-1] < b <= A[idx]
        C.append(closer(A[clip(idx - 1)], A[clip(idx)], b))
    return C
```

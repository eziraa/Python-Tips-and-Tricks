## Flatten-Nested-List
- To flatten nested list we can use three methods

### 1 By using for loop and extend

```python

nested_list = [[1, 2, 3], [4, 5], [5, 6, 7]]

flattend_list = []
for inner_list in nested_list:
    flattend_list.extend(inner_list)

print(flattend_list)

# output [1, 2, 3, 4, 5, 5, 6, 7]
```

### 2 By using itertools module

```python
import itertools

flattend_list = list(itertools.chain.from_iterable(nested_list))

print(flattend_list)

# output [1, 2, 3, 4, 5, 5, 6, 7]
```
### 3 By Using list comprehension.
```python
flattend_list = [i for inner_list in nested_list for i in inner_list]

print(flattend_list)

# output [1, 2, 3, 4, 5, 5, 6, 7]
```
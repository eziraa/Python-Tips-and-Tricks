## Index of largest and smalles number in list

- To get the index of largest and smallest number in list we use `enumerate`, `max` and `min` function
- `enumerate` function a list of the pair of list items with thier index
- The `lambda` function used to specify the key to comparision in max function

## Biggest number index

```python
numbers = [1, 4, 6, 7, 8, 5, 23, 7, 0, 9]

max_num_pairs = max(enumerate(numbers, start=0), key=lambda x: x[1])
max_num_index = max_num_pairs[0]

print(max_num_index)  # output 6
```

## Smallest number index
```python
min_num_pairs = min(enumerate(numbers, start=0), key=lambda x: x[1])
min_num_index = min_num_pairs[0]

print(min_num_index)  # output 8
```
## NLargest and NSmallest

- To get NLargest or NSmallest we can use `sort` method and slicing

```python
import heapq
numbers = [2, 4, 5, 6, 7, 8, 86, 6, 5]
numbers.sort()
n_largest = numbers[-5:]
print(n_largest)  # output [6, 6, 7, 8, 86]

n_smallest = numbers[:5]
print(n_smallest)  # output [2, 4, 5, 5, 6]
```

- But the code above is less readable to make the code more readable we can use `heapq` builtin module
```python

numbers = [2, 4, 5, 6, 7, 8, 86, 6, 5]
n_largest = heapq.nlargest(5, numbers)
print(n_largest)  # output [6, 6, 7, 8, 86]

n_smallest = heapq.nsmallest(5, numbers)

print(n_smallest)  # output [2, 4, 5, 5, 6]
```
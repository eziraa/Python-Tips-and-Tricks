## Sorting list
- By default is ascending order but we can change by setting the parameter of sort method

- List can be sorted only if ot contain the same data type
- sort mothed modify the orginal list rather tan retunring new list

```python
numbers = [1, 2, 5, 3, 6, 4]
numbers.sort()
print(numbers)  # output [1,2,3,4,5,6]

numbers.sort(reverse=True)

print(numbers)  # output [6,5,4,3,2,1]
```
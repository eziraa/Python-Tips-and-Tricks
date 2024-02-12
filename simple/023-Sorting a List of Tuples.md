## Sorting a List of Tuples
- We can sort a list of tuples by using `sorted` function and by passing `itemgetter` function from `operator` moduleas the `key` parameter of `sorted` function (second parameter)

```python
from operator import itemgetter

list_of_tuples = [('Peter', 'Paul'), ('Ezira', 'Tigab'), ('Henok', 'Henon'),
                  ('Simon', 'Titus')]


sorted_list_of_tuples = sorted(
    list_of_tuples, key=itemgetter(0))

print('Sorted by first name')
print(sorted_list_of_tuples)

sorted_list_of_tuples = sorted(list_of_tuples, key=itemgetter(1))
print('Sorted by second name')
print(sorted_list_of_tuples)

# output
# Sorted by first name
# [('Ezira', 'Tigab'), ('Henok', 'Henon'), ('Peter', 'Paul'), ('Simon', 'Titus')]
# Sorted by second name
# [('Henok', 'Henon'), ('Peter', 'Paul'), ('Ezira', 'Tigab'), ('Simon', 'Titus')]
```
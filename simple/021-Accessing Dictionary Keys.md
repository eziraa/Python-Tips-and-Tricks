## Accessing Dictionary Keys
- We can access dictionary keys in the three differennt ways

1. By using list comprehension
```python
dict1 = {
    'name': 'Ezira',
    'nikename': 'sutual',
    'department': 'Software Engineering',
    'age': 22,
    True: 'all'
}

dict1_keys = [key for key in dict1.keys()]

print(dict1_keys)

# output
# ['name', 'nikename', 'department', 'age', True]
```

2. by converting to set by using `set`function

```python
dict1 = {
    'name': 'Ezira',
    'nikename': 'sutual',
    'department': 'Software Engineering',
    'age': 22,
    True: 'all'
}

dict1_keys = set(dict1)

print(dict1_keys)

# output
# {True, 'age', 'nikename', 'name', 'department'} but the order not guarranted
```
3. By using `sorted` function only work for the same datatype keys

```python
dict1 = {
    'name': 'Ezira',
    'nikename': 'sutual',
    'department': 'Software Engineering',
    'age': 22,
}

dict1_keys = sorted(dict1)

print(dict1_keys)
# ['age', 'department', 'name', 'nikename']
```
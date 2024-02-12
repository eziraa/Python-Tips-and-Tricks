## Iterable or Not
- we can check weathe an object is iterable or nor

- By uning `iter` method if it is not itrable it raise `TypeError` exception

```python
obj1 = [1, 3, 4, 6, 7]

try:
    obj1 = iter(obj1)
except TypeError:
    print('Object not itrable')
else:
    print('object is iterable')

obj2 = 9.5

try:
    obj1 = iter(obj2)
except TypeError:
    print('Object not itrable')
else:
    print('object is iterable')

# output
# object is iterable
# Object not itrable
```
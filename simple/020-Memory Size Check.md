## Memory Size Check
- We can check the memory size of our data like string, list, tuple, dict

1.  By importing `sys` module and by using `getsizeof` method in this module

```python
import sys

list1 = ['Ezira', 'Sutual', 'Yallew', 'Eyasu']
tuple1 = ('Ezira', 'Sutual', 'Yallew', 'Eyasu', 'Henok')
str1 = 'We all poeple of ...'
dict1 = {
    'name': 'Ezira',
    'department': 'Software Engineering',
    'age': 22
}

print(f'size of list1 is {sys.getsizeof(list1)}')
print(f'size of tuple1 is {sys.getsizeof(tuple1)}')
print(f'size of str1 is {sys.getsizeof(str1)}')
print(f'size of dict1 is {sys.getsizeof(dict1)}')

# output
# size of list1 is 88
# size of tuple1 is 80
# size of str1 is 61
# size of dict1 is 184
```
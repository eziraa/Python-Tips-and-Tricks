## Counting occurance

- To count the occurance of an item in iterable we can use `counter` class from `collections` module
- This class return the dictionary of how many time each item occur in the iterable and the item
- Then to get the occurance we can use `get` method or [] with key the item itself

```python
from collections import Counter

list = ['Ezira', 'Sutual', 'Eliyas', 'Solomon', 'Ezira']

count_ezira = Counter(list).get('Ezira')

print(f'The name Peter appears in the list '
      f'{count_ezira} times.')
```
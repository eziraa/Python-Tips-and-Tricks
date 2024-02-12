## Most Frequent in a String

1. We can find the  most frequent element in string by using `max` function by passing a callback function `count`

```python
str1 = 'give more for more'

frequented_elem = max(str1, key=str1.count)

print(frequented_elem)  # out put `e`

# remember the max function return the first most repeated if there is more than one most repeated elements
```

 2. By using `most_common` method `Counter` class of `collections` module

```python
from collections import Counter

str2 = 'kjjkenwfejler'

repeated_elems = Counter(str2).most_common(1)  # if we want only one most

print(repeated_elems)  # output `[('j', 3)]`
```
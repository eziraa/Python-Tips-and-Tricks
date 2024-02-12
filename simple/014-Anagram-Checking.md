## Checking Anagram
- To check waether the two strings are `anagram` we can use the following two methods

### 1 By using `Counter` from `collections` module

```python
from collections import Counter

str1 = 'lost'
str2 = 'stol'
are_anagram = Counter(str1) == Counter(str2)
print(are_anagram)      # output True
```
### 2 by using `sorted` method not `sort` because `sorted` order the element ascendingly
```python
str1 = 'lost'
str2 = 'stot'
are_anagram = sorted(str1) == sorted(str2)
print(are_anagram)      # output False
```
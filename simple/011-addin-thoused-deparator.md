## Adding thounsend separator
- if we are working on very large number we cn add thousend separator or underscore

### A Adding thounsend separator
```python
numbers = [10989767, 9876780, 9908763]

a_formatted = ['{:,}'.format(num) for num in numbers]

print(a_formatted)     # out put ['10,989,767', '9,876,780', '9,908,763']
```
### Adding underscore operator by using f-string
```python
numbers = [10989767, 9876780, 9908763]

a_formatted = [f'{num:_}' for num in numbers]
print(a_formatted)      # output ['10_989_767', '9_876_780', '9_908_763']
```
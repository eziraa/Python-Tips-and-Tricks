## Absolute Value

- For absolute value we can use `abs` function

### `abs` in list

```python
numbers = [2, -8, 5, -6, -4]
positive_numbers = [abs(i) for i in numbers]

print(positive_numbers)  # output[ 2,8,5,6,4]
```
### `abs` in complex number
- When we use `abs` in complex number it convert to magnitude of the complex number
```python
complex_num = 6 + 3j
print(abs(complex_num))  # output 6.708203932499369
```
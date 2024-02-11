## Python print function behavior

The `print` function in Python by default displays its content in one line and ends with a newline character (`\n`). This default behavior can be altered using parameters such as `end`.

### Displaying values horizontally

To display values horizontally, especially when iterating over iterable objects, the `end` parameter can be utilized. Here's an example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7]

for num in numbers:
    print(num, end="")  # output 1234567

```

## Separating Arguments
The print function also has a sep parameter to separate its arguments. For example:

```python
print('02', '05', '2024', sep='/')  # Output: 02/05/2024
```
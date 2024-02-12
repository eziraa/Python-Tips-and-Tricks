## `startwith` and `endwith`
- Those methods return true if the string bigin with or end with the specified string
- `startwith` and `endwith` in list to group list items

### `startswith` in list

```python
persons = ['Simon', 'Peter', 'David', 'Ezira', 'Eysu']

e_starter = [person for person in persons if person.startswith('E')]
print(e_starter)    # output ['Ezira', 'Eysu']
```
### `endswith` in list
```python
persons = ['Simon', 'Peter', 'David', 'Ezira', 'Eysu', 'Epha']

a_finish = [person for person in persons if person.endswith('a')]

print(a_finish)  # output ['Ezira', 'Epha']
```
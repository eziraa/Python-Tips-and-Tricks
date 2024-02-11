## Dictionary Merging
 if we have to separate dictionaries how to merge those and have exaclty one dictioanry

### First method using '|' operator

```python
author_data1 = {
    'name': 'ezira',
    'age': 22,
    'gender': 'M'
}
author_data2 = {
    'department': 'Software Engineering',
    'Skills': ['Web Design', 'Web Developement', 'Data Analysis']
}

full_author_data1 = author_data1 | author_data2
print(full_author_data1)
```

###  Method two by using `**` operator
```python
full_author_data2 = {**author_data1, **author_data2}
print(full_author_data2)
```

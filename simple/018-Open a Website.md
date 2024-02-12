## Open a Website Using Python
- We can open a website by using builtin module called `webbrowser`

```python
import webbrowser

url = 'https://chat.openai.com/'
openurl = webbrowser.open(url)

# open method of webbrowser return true if it open
print(openurl)  # True or  False

# And we can open new tap by using `open_new` method

webbrowser.open_new(url)
```
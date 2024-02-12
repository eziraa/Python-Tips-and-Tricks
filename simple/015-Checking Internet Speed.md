## Checking Internet Speed

- We can check internet speed of our machine by using `speedtest` module
- Before write the python code we have to install 'speedtest-cli' module

```bash
 pip install speedtest-cli
```
1. Test download speed the speed we get is in `bits` so we have to divide in 8000000 to convert to `mb`

```python
import speedtest

download_speed = speedtest.Speedtest()

print(f'Download speed is {download_speed.download() / 8000000:.f}MB')

# Test upload speed


download_speed = speedtest.Speedtest()

print(f'Download speed is {download_speed.upload() / 8000000:.f}MB')

```
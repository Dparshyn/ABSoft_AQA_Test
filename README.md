# ABSoft_AQA_Test
Test case for Junior AQA vacancy in AB Soft
##

# Description:
Test case based on Selenium and PyTest provides such functionality:
open selected browser window, go to [link](https://getnada.com"), find generated random mailbox-name
request for random API for generating links
sending message to generated above mailbox with this links
waiting for income our message, opened a message and checks content for links existing


# System Requirements:
* Python 3.6 or higher
* Browser Opera 69.0.3686.77 (it also works with Google Chrome)
* Opera Webdriver 83.0.4103.97
* OS - Windows 10 Pro (it also tested on macOS Catalina 10.15.6)


# How to install and setup:
First of all if you need to check that Opera browser installed and `Webdriver` is updated. 
Binaries are available under [the releases tab](https://github.com/operasoftware/operachromiumdriver/releases).
If you will use Google Chrome browser you need to copy latest version of ChromeDriver in project directory or use valid PATH to Driver as shown in project:
```python
# Create ChromeDriver service:
from selenium import webdriver
webdriver.Chrome(executable_path="('path/to/webdriver')")
```

Latest [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) version. 

Also you need to install required libraries and frameworks listed in `requirements.txt` file by using command in your bash (please check that you start your bash in working directory):

```
$ pip install -r requirements.txt
```
Please run the test by using bash-command (You will need to input password to mailbox `absofttest67@gmail.com` that was sent to HR Manager yet):
```
$ pytest -s test_send_mail.py
```

Due to domain with [Random Cat](https://aws.random.cat/meow) is unavailable while developing this test, URL-generating for this link was skipped.


**If you have any questions, please do not hesitate to contact me anytime :) **
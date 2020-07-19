# ABSoft_AQA_Test
Test case for Junior AQA vacancy
##
# Description:
Test case based on Selenium and PyTest 

# System Requirements:
* Python 3.6+
* Google Chrome 84.0.4147.89
* ChromeDriver 84.0.4147.30
* OS - macOS Catalina 10.15.6 (but should works on other OS as well)


# How to install and setup:
First of all you need to copy latest version of ChromeDriver in project directory or use valid PATH to Driver as shown in project:
```
webdriver.Chrome(executable_path=**"./chromedriver"**)
```
Latest driver version you can find here https://chromedriver.chromium.org/downloads 

You need to install required libraries and frameworks listed in requirements.txt file by using command in your bash (please check that you start your bash in working directory):

```
$ pip install -r requirements.txt
```
Please run the test by using bash-command:
```
$ pytest -v -s test_send_mail.py
```

Due to domain https://aws.random.cat/meow is unavailable while developing this test, 

**Enjoy it and have a nice mood (^.^)**


# OrangeHRM Dummy Testing

Dummy Live Url: <a href="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login">Click to visit Website</a>

## How to Run the Test
* Clone the repository
* Install the required packages
  * `pip install -r requirements.txt`
* Run the test
```commandline
pytest -v -s --html=.\reports\report.html .\tests\home\test_login.py --browser firefox
```
* Open the report
  * Open the report from the reports folder

## Test Cases
* Valid Login
* Invalid Login

## Test Data
* Valid Login
  * Username: admin
  * Password: admin123
    * Expected Result: Login should be successful
  
* Invalid Login
  * Username: User
  * Password: user123
    * Expected Result: Login should fail

## Test Steps
* Valid Login
  * Open Browser
  * Navigate to URL
  * Enter Username
  * Enter Password
  * Click on Login
  * Verify Dashboard

* Invalid Login
  * Open Browser
  * Navigate to URL
  * Enter Username
  * Enter Password
  * Click on Login
  * Verify Error Message

### Test Features
* Selenium with Python
* Pytest Framework
* Page Object Model
* Pytest-html Report
* Login Data Driven Testing
  * Data from CSV
  * Data from .env file
* Cross-Browser Testing
  * Chrome
  * Firefox
  * Edge
* Parallel Testing
* Jenkins Integration






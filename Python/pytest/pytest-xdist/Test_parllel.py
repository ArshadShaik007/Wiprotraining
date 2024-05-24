import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def testcase1():
    print("testcase 1")
    option=webdriver.EdgeOptions()
    driver=webdriver.Edge(options = option)
    driver.maximize_window()
    driver.get("https://www.google.com")

# test case 2
def testcase2():
    print("testcase 2")
    option=webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("https://www.facebook.com")

# test case 3
def testcase3():
    print("testcase 3")

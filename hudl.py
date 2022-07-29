from cmath import log
from tkinter import Button
from xml.dom.minidom import Element
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
# navigate to URL
driver.get("https://www.hudl.com/")
#Define elements
lbutton = "//a[contains(text(), 'Log in')]"
email = "//input[contains(@id,'email')]"
password = "//input[contains(@id,'password')]"
submitbtn = "//button[contains(text(), 'Log In')]"
logInBtnText = "//button[contains(text(), 'Log In with an Organization')]"
needHelpbtn = "//a[contains(text(), 'Need help?')]"
pwdReset = "//button[contains(text(), 'Send Password Reset')]"

#click login button
loginbtn = driver.find_element(By.XPATH, lbutton)
loginbtn.click()
#Enter your static email and password
enterEmail = driver.find_element(By.XPATH, email)
enterEmail.send_keys("bmutebi2@gmail.com")
enterPwd = driver.find_element(By.XPATH, password)
enterPwd.send_keys("test123")
#Check the Login with an Org button is displayed
checkLogBtnOrg = driver.find_element(By.XPATH, logInBtnText)
print(checkLogBtnOrg.is_displayed)
#Click Submit button
clickSubmit = driver.find_element(By.XPATH, submitbtn)
clickSubmit.click()
#Click Need Help
Help = driver.find_element(By.XPATH, needHelpbtn)
Help.click()
#Click Reset Password button
resetPwd = WebDriverWait(driver, timeout=10).until(driver.find_element(By.XPATH, pwdReset))
assert resetPwd.text == "Send Password Reset"
resetPwd.click()
#close chrome driver
driver.close()
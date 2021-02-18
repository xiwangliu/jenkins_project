from time import sleep

from appium import webdriver
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(4)

print(driver.current_package)
print(driver.current_activity)

driver.start_activity("com.android.mms",".ui.ConversationList")
sleep(2)
print(driver.current_package)
print(driver.current_activity)
driver.quit()

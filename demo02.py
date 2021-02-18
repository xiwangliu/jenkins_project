from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# sleep(4)

# if driver.is_app_installed("com.tpshop.malls"):
#     driver.remove_app("com.tpshop.malls")
# else:
#     driver.install_app(r'C:\Users\86187\Desktop\tpshop.apk')
# driver.background_app(3)

# driver.find_element_by_id("com.android.settings:id/search").click()
# sleep(2)
# driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
# sleep(2)
# driver.find_element_by_xpath("//*[@class='android.widget.ImageButton']")

# first_element = driver.find_element_by_xpath("//*[@text='Storage']")
# second_element = driver.find_element_by_xpath("//*[@text='More']")

# TouchAction(driver).tap(driver.find_element_by_xpath("//*[@text='Wi‑Fi']")).perform()
# TouchAction(driver).tap(x=650,y=650).perform()

# TouchAction(driver).press(driver.find_element_by_xpath("//*[@text='Wi‑Fi']")).release().perform()

# TouchAction(driver).\
#     tap(driver.find_element_by_xpath("//*[@text='Wi‑Fi']")).\
#     long_press(x=460,y=792,duration=2000).release().perform()
print(driver.get_window_size())

print(driver.get_window_size()['width'])

driver.get_screenshot_as_file(r"/Users/86187/Desktop/adb.png")

sleep(2)

# driver.swipe(100,2000,100,1000)


driver.quit()
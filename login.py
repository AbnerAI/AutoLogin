from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver_path = 'C:/Users/win/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# 这里是你的登录信息
username = 'bnu学号'  # 你的用户名
password = '密码'  # 你的密码

# 启动WebDriver
driver = webdriver.Chrome()

# 打开登录页面
driver.get("http://172.16.202.201/srun_portal_pc?ac_id=1&theme=bnu")

# 等待页面加载
time.sleep(2)

# 填写用户名和密码
# 注意：这里的'id'（例如'username_field'和'password_field'）需要根据实际页面的元素进行替换
driver.find_element("id", "username").send_keys(username)
driver.find_element("id", "password").send_keys(password)

# 提交表单（假设登录按钮的id是'login_button'）
driver.find_element("id", "login-account").click()

# 等待一段时间让登录操作完成
time.sleep(5)

# 关闭浏览器
driver.quit()


# Ajax Hook Demo






```
0.Demo 执行步骤：

1.安装requirements.txt 
pip3 install -r requirements.txt 

2.打开一个终端
执行 python3 server.py


3.打开另一个终端
执行 python3 auto.py


done!

```


```
0.实现代码
1、hook.js
监听 XMLHttpRequest 请求

// 打开链接，复制代码到这里
// https://unpkg.com/ajax-hook@2.0.3/dist/ajaxhook.min.js
// https://unpkg.com/axios/dist/axios.min.js


ah.proxy({
  //请求成功后进入
  onResponse: (response, handler) => {
    if (response.config.url.startsWith('/api/movie')) {
      axios.post('http://localhost:5000/receiver/movie', {
        url: window.location.href,
        data: response.response
      })
      console.log(response.response)
      handler.next(response)
    }
  }
})


2.auto.py

驱动chrome

# pip3 install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://dynamic6.scrape.center/')
driver.execute_script(open('hook.js').read())
time.sleep(2)

for index in range(10):
    print('current page', index)
    btn_next = driver.find_element(By.CSS_SELECTOR, ".btn-next")
    btn_next.click()
    time.sleep(2)


driver.close()
driver.quit()


3、server.py

接收数据的服务，可以进一步将数据存入数据库

import json

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/receiver/movie', methods=['POST'])
def receive():
    content = json.loads(request.data)
    print(content)
    # to something
    return jsonify({'status': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


```


```

0.备注：

1.生成requirements.txt 
pip3 freeze > requirements.txt

2.selenium的webdriver问题

	0.DeprecationWarning: executable_path has been deprecated selenium python
	# pip install webdriver-manager
	from selenium import webdriver
	from selenium.webdriver.chrome.service import Service
	from webdriver_manager.chrome import ChromeDriverManager
	from selenium.webdriver.common.by import By

	s=Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=s)
	driver.maximize_window()
	driver.get('https://www.google.com')
	driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')

	1.DeprecationWarning: find_element_by_* commands are deprecated. Please use find_element() instead
	Solution
	Instead you have to use find_element(). As an example:

	You have to include the following imports

	from selenium.webdriver.common.by import By

	Using class_name:

	button = driver.find_element_by_class_name("quiz_button")
	Needs be replaced with:

	button = driver.find_element(By.CLASS_NAME, "quiz_button")
	In similar lines you also have to change the following:

	Using id:

	element = find_element_by_id("element_id")
	Needs be replaced with:

	element = driver.find_element(By.ID, "element_id")
	Using name:

	element = find_element_by_name("element_name")
	Needs be replaced with:

	element = driver.find_element(By.NAME, "element_name")
	Using link_text:

	element = find_element_by_link_text("element_link_text")
	Needs be replaced with:

	element = driver.find_element(By.LINK_TEXT, "element_link_text")
	Using partial_link_text:

	element = find_element_by_partial_link_text("element_partial_link_text")
	Needs be replaced with:

	element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
	Using tag_name:

	element = find_element_by_tag_name("element_tag_name")
	Needs be replaced with:

	element = driver.find_element(By.TAG_NAME, "element_tag_name")
	Using css_selector:

	element = find_element_by_css_selector("element_css_selector")
	Needs be replaced with:

	element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")
	Using xpath:

	element = find_element_by_xpath("element_xpath")
	Needs be replaced with:

	element = driver.find_element(By.XPATH, "element_xpath")

```

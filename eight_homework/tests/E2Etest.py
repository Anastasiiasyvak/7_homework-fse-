from selenium import webdriver

driver = webdriver.Chrome(executable_path='PycharmProjects/7_homework(fundamentals_Software_engineering)/eight_homework/chromedriver_path')

app_url = 'http://209.97.181.107:8000'
driver.get(app_url)

reports_url = app_url + '/api/reports'
driver.get(reports_url)

element = driver.find_element_by_id('df60f3f8-0e13-b64a-76b5-863bae54478e')

expected_text = 'Expected Text'
assert element.text == expected_text

driver.quit()

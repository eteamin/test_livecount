from selenium import webdriver
import requests
import socket


actual_id_max_value_pair = {}
expected_id_max_value_pair = {}

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://beta.varzesh3.com/news/live')
    all_view_counts_list = driver.find_elements_by_xpath("//*[@id='main']/ul/li")
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(('94.182.163.202', 1234))
    socket_client.send()
    data = socket_client.recv(16)
    live_count_data = socket
    for list in all_view_counts_list:
        list_id = list.get_attribute('id')
        list_max_value = list.find_elements_by_tag_name('div')[0].get_attribute('data-maxvalue')
        actual_id_max_value_pair[list_id] = list_max_value

    for item in live_count_data:
        expected_id_max_value_pair[item['Id']] = item['ViewCount']



    print(1)









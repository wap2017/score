from PIL import Image
from selenium import webdriver
import time


def get_snap(driver):  # 这个函数是截全屏的
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj


def get_image(driver):
    # TODO 如果爬取的网页有iframe，则切换到xpath对应的iframe，没有的话，下面一行代码可以注释
    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td[2]/div[1]/table/tbody/tr/td/iframe"))
    driver.find_element_by_id("txt_sdertfgsadscxcadsads").click() # TODO 这里是点击输入验证码框才会显示验证码
    time.sleep(2)
    img = driver.find_element_by_id('imgCode')
    location = img.location
    print(location)
    size = img.size
    left = location['x'] + 10  # TODO 这里根据自己爬取的网站进行调整，如果没有iframe的，不需要手工调整
    top = location['y'] + 107
    right = left + size['width']
    bottom = top + size['height']
    page_snap_obj = get_snap(driver)
    page_snap_obj.show()
    image_obj = page_snap_obj.crop((left, top, right, bottom))

    image_obj.show()
    return image_obj  # 得到的就是验证码


if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "http://****/"  # TODO 这里换成你想抓取验证码的网址
    driver.get(url)
    get_image(driver)

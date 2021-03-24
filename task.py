import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException


class Scraper:

    def __init__(self):
        self.options = Options()
        self.options.page_load_strategy = 'normal'
        self.chrome_path = "chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_path, options=self.options)
        # self.pause_time = 1

    def extract_data_from_page(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://store.hp.com/us/en/pdp/hp-laptop-15t-dy200-2j130av-1")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[@id='onetrust-close-btn-container']").click()
        time.sleep(1)
        action = ActionChains(driver)
        review = driver.find_element_by_xpath("//ul[@class='pdp-tabs-nav clearfix']").find_element_by_id("tab_5")
        action.move_to_element(review).perform()
        review.click()
        heading = driver.find_element_by_xpath("//ol[@class='bv-content-list bv-content-list-reviews']").find_element_by_class_name("bv-content-title").text.strip()

        driver.quit()
        return heading


if __name__ == "__main__":
    scraper = Scraper()
    print(scraper.extract_data_from_page())

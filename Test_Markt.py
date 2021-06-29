import unittest
from Markt import *

class Testimage(unittest.TestCase):
    def test_website_data(self):
        '''Testing data collected from website'''
        webdriver_path = 'C:/Users/Kalyan/Downloads/vaccipy-windows/tools/chromedriver/chromedriver-windows.exe'
        browser = webdriver.Chrome(webdriver_path)  # open the chrome browser
        browser.get("https://www.wollplatz.de/")
        search_bar = browser.find_element_by_name('txtSearch')
        search_bar.send_keys("DMC Natura XL")
        search_bar.send_keys(Keys.RETURN)

        item_prices = browser.find_elements_by_class_name('product-price')
        for price in item_prices:
            prices_list.append(price.text)
        result= prices_list[0]
        self.assertEqual(result,'€ 1,05')

    def test_save_data(self):
        '''Testing data saved in file'''
        data = pd.read_csv("wooldata.csv")
        result = data['Name'][0]
        self.assertEqual(result,'Drops Safran 1 Light-pink')

if __name__ == '__main__':
    unittest.main()
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import pandas as pd

class Wool:
    global brands_list,prices_list,times_list, needlesize_list, compilation_list, heading_list
    brands_list = prices_list = times_list = needlesize_list = compilation_list = []
    heading_list = ['Name','Price','Time','NeedleSize','Compilation']

    def website_data(self, website_url, brand, description):
        '''collect data from website'''
        webdriver_path = 'C:/Users/Kalyan/Downloads/vaccipy-windows/tools/chromedriver/chromedriver-windows.exe'
        browser = webdriver.Chrome(webdriver_path)                        # open the chrome browser
        browser.get(website_url)
        search_bar = browser.find_element_by_name('txtSearch')
        search_bar.send_keys(brand + " " + description)
        search_bar.send_keys(Keys.RETURN)

        item_brands       = browser.find_elements_by_id('pageheadertitle')
        item_prices       = browser.find_elements_by_class_name('product-price')
        time_html_list    = browser.find_element_by_class_name('fa-ul')
        items             = time_html_list.find_elements_by_tag_name("li")
        item_delitime     = items[2]
        item_needlesizes  = browser.find_elements_by_xpath('//*[@id="pdetailTableSpecs"]/table/tbody/tr[5]/td[2]')
        item_compilations = browser.find_elements_by_xpath('//*[@id="pdetailTableSpecs"]/table/tbody/tr[4]/td[2]')

        for brand in item_brands:
            brands_list.append(brand.text)
        for price in item_prices:
            prices_list.append(price.text)
        times_list.append(item_delitime.text)
        for size in item_needlesizes:
            needlesize_list.append(size.text)
        for compilation in item_compilations:
            compilation_list.append(compilation.text)

    def save_data(self):
        '''Save collected website data into a dataframe to display onto the screen and also to save into a file'''
        dfL = pd.DataFrame(zip(brands_list, prices_list, times_list, needlesize_list, compilation_list),columns=heading_list)
        dfL.to_csv(path_or_buf='C:/Users/Kalyan/Desktop/Markt-Pilot/wooldata.csv', columns=heading_list)
        print(dfL)

if __name__ == '__main__':
    obj1 = Wool()
    obj1.website_data("https://www.wollplatz.de/","Drops","Safran")
    obj1.save_data()

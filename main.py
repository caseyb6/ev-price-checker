import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from brands import *

def get_vehicle_info():
    vehicle_list = ['S','3','y']
    vehicle_info_df = pd.DataFrame(columns=['vehicle_name','vehicle_trim','vehicle_price'])

    for v in vehicle_list:
        url = Tesla(model=v).get_listing_url(zip_code='53202',distance_from_zip=200)

        tesla_vehicle_name_selector = Tesla.vehicle_name_selector
        tesla_vehicle_price_selector = Tesla.vehicle_price_selector
        tesla_vehicle_trim_selector = Tesla.vehicle_trim_selector

        opts = Options()
        opts.add_argument('--headless')
        browser = Chrome(options=opts)
        browser.get(url)

        vehicle_name_object = browser.find_elements(By.CSS_SELECTOR,tesla_vehicle_name_selector)
        vehicle_trim_object = browser.find_elements(By.CSS_SELECTOR,tesla_vehicle_trim_selector)
        vehicle_price_object = browser.find_elements(By.CSS_SELECTOR,tesla_vehicle_price_selector)

        vehicle_names = [obj.text for obj in vehicle_name_object]
        vehicle_trims = [obj.text for obj in vehicle_trim_object]
        vehicle_prices = [obj.text for obj in vehicle_price_object]

        model_df = pd.DataFrame({'vehicle_name':vehicle_names,'vehicle_trim':vehicle_trims,'vehicle_price':vehicle_prices})
        vehicle_info_df = pd.concat([vehicle_info_df,model_df])
    
    print(vehicle_info_df.reset_index())
    
get_vehicle_info()
from selenium import webdriver; from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, re, sys, pyautogui as pag
import pyperclip as pyp

# User Validation
first_verification = pag.confirm(text="You have opened a file for VERIFIED USER.\nIf you are USER, or have his permissions, please continue.\nIf not, please seek a supervisor for assistance.", buttons=["Continue", "Cancel"])
if first_verification == "Cancel":
    sys.exit()
else:
    user_name = pag.prompt(text="Input User Name:", title="User Validation", default="default-username")
    password = pag.password(text="Input Password:", title="User Validation", default="default-password", mask='*')
    users_name = "default-username"
    user_password = "default-password"

def remove_html_tags(get_price):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', get_price)

def shop_1(sku):
    try:
        WINDOW_SIZE = "1920,1080"
        base_url = "https://www.website.com/product/"
        product_url = base_url+str(sku)
        eldir = 'XPATH'
        chrome_options = Options()
        # Enable Headless Mode
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        driver.get(product_url)
        time.sleep(1)
        get_price = driver.find_element(By.XPATH, eldir).get_attribute('outerHTML')
        time.sleep(1)
        driver.close()
        price = (remove_html_tags(get_price))
        pag.alert(text="The price is "+price, title="Price Found: Added to Clipboard", button="Ok")
        pyp.copy(str(price))

    except Exception as exe:
        print("There was an Error: "+exe)

def shop_2(sku):
    try:
        WINDOW_SIZE = "1920,1080"
        base_url = "https://www.website.com/product"
        product_url = base_url+str(sku)
        eldir = 'XPATH'
        chrome_options = Options()
        # Enable Headless Mode
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
        driver.get(product_url)
        time.sleep(3)
        get_price = driver.find_element(By.XPATH, eldir).get_attribute('outerHTML')
        time.sleep(3)
        driver.close()
        price = (remove_html_tags(get_price))
        pag.alert(text="The price is "+price, title="Price Found: Added to Clipboard", button="Ok")
        pyp.copy(str(price))

    except Exception as exe:
        print("There was an Error: "+exe)

def get_price():
    if user_name == users_name and password == user_password:
        sku = pag.prompt(text="Please input the SKU: ", title="USERNAME's Personal Price Finder", default="")
        shop = pag.confirm(text = "Select which site you wish to search: ", title="USERNAME's Personal Price Finder", buttons=['Shop_1', 'Shop_2', 'Cancel'])
        search_for = pag.confirm(text="Select which item you are searching for: ", title="USERNAME's Personal Price Finder", buttons=['Price', 'Cancel'])
        try:
            if shop != "Cancel" or search_for != "Cancel":
                if shop == 'Shop_1':
                    shop_1(sku)
                elif shop == 'Shop_2':
                    shop_2(sku)
                else:
                    print("How the fuck did you mess this up?")
            else:
                pag.alert(text="This action has been canceled. Please run this file again if necessary.", title="Price Finder")
        except Exception as exc:
            print(exc)
get_price()

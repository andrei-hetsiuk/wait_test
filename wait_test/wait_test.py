
class TestBasket():

    def test_account_add_new_name(self, browser):
        #browser.implicitly_wait(5)
        browser.maximize_window()

        try:
            browser.get("http://suninjuly.github.io/explicit_wait2.html")
            
            button = WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, 'price'), str('$100')))
            button = browser.find_element_by_id("book").click()
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            x = browser.find_element_by_id("input_value").text
            y = calc(x)
            button = browser.find_element_by_id("answer")
            button.send_keys(y)
            button = browser.find_element_by_id("solve").click()
        
    
	
        finally:
            time.sleep(5)
            #browser.quit()
               
            

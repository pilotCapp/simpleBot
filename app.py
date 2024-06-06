from playwright.sync_api import sync_playwright

def main(email,amount,link,card_number,expire_date,cvc,name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        #page.viewport_size = {"width": 1200, "height": 800} 
    
        # Open the website
        page.goto(link)
    
        # Click a button automatically
        button_selector = 'text="Kjøp billett"'  # Replace with the actual selector of the button
        button = page.wait_for_selector(button_selector, timeout=300000)  # Timeout in milliseconds
        page.click(button_selector)
        
        member_row_xpath = '//tr[td[contains(text(), "Medlem")]]'
        member_dropdown_selector = f'{member_row_xpath}//select[@tabindex="1"]'

        # Select the option in the dropdown for members
        page.wait_for_selector(member_dropdown_selector)
        page.select_option(member_dropdown_selector, label=amount)
        
        #page.screenshot(path='screenshots/email.png', selector='#email')
        textbox = page.locator('#email, #form_email')
        textbox.click()
        textbox.type(email)

        # Simulate typing the desired text
        
        checkout_button_selector = '//*[@type="submit"]' 
        page.wait_for_selector(checkout_button_selector)
        page.click(checkout_button_selector)
        
        
        card_number_input_selector = 'input#cardNumber'
        card_expiry_input_selector = 'input#cardExpiry'
        card_cvc_input_selector = 'input#cardCvc'
        card_name_input_selector = 'input#billingName'
        submit_button_selector = '//*[@type="submit"]'

        page.wait_for_selector(card_number_input_selector,timeout=300000)
        page.fill(card_number_input_selector, card_number)
        page.wait_for_selector(card_expiry_input_selector)
        page.fill(card_expiry_input_selector, expire_date)
        page.wait_for_selector(card_cvc_input_selector)
        page.fill(card_cvc_input_selector, cvc)
        page.wait_for_selector(card_name_input_selector)
        page.fill(card_name_input_selector, name)
        page.wait_for_selector(submit_button_selector)
        page.click(submit_button_selector)

        page.wait_for_timeout(50000)
        
        # You can also wait for something to happen after the click
    
        # Close the browser
        browser.close()
            
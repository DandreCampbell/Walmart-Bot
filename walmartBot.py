from selenium import webdriver
import time

class PS5Bot:

    def __init__(self, firstName, lastName, email, streetAddress, city, zipCode, phone, creditCardNumber,
                creditCardMonth, creditCardYear, creditCardCCV, PATH):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.streetAddress = streetAddress
        self.city = city
        self.zipCode = zipCode
        self.phone = phone
        self.creditCardNumber = creditCardNumber
        self.creditCardMonth = creditCardMonth
        self.creditCardYear = creditCardYear
        self.creditCardCCV = creditCardCCV
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942')

    def add_ps5_to_cart_and_checkout(self):
        addToCart = '//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span'
        checkOut = ('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/'
        'div[3]/div/div/div[2]/div/div[2]/div/button[1]')
        continueWithoutAccount = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]'
        '/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span')
        self.clickButton(addToCart)
        self.clickButton(checkOut)
        self.clickButton(continueWithoutAccount)

    def filling_shipping_info(self):
        firstContinue = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/'
        'div/div/div/div[3]/div/div/div[2]/button/span')
        firstName ='//*[@id="firstName"]'
        lastName = '//*[@id="lastName"]'
        email = '//*[@id="email"]'
        streetAddress = '//*[@id="addressLineOne"]'
        city = '//*[@id="city"]'
        zipCode = '//*[@id="postalCode"]'
        phone = '//*[@id="phone"]'
        confirmInfo = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/'
        'div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button/span')
        self.clickButton(firstContinue)
        self.enterData(firstName, self.firstName)
        self.enterData(lastName, self.lastName)
        self.enterData(email, self.email)
        self.enterData(streetAddress, self.streetAddress)
        self.enterData(city, self.city)
        self.enterData(zipCode, self.zipCode)
        self.enterData(phone, self.phone)
        self.clickButton(confirmInfo)

    def fill_out_payment_and_order(self):
        creditCardNum = '//*[@id="creditCard"]'
        creditExpireMonth = '//*[@id="month-chooser"]'
        creditExpireYear = '//*[@id="year-chooser"]'
        creditCVV = '//*[@id="cvv"]'
        reviewOrder = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div'
        '/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button/span/span/span')
        self.enterData(creditCardNum, self.creditCardNumber)
        self.enterData(creditExpireMonth, self.creditCardMonth)
        self.enterData(creditExpireYear, self.creditCardYear)
        self.enterData(creditCVV, self.creditCardCCV)
        self.clickButton(reviewOrder)

    def clickButton(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception:
            time.sleep(1)
            self.clickButton(xpath)

    def enterData(self, field, data):
        try:
            self.driver.find_element_by_xpath(field).send_keys(data)
            pass
        except Exception:
            time.sleep(1)
            self.enterData(field, data)

if __name__ == "__main__":
    personal_info = dict(
        firstName = "",
        lastName = "",
        email = "",
        streetAddress = "",
        city = "",
        zipCode = "",
        phone = "",
        creditCardNumber = "",
        creditCardMonth = "",
        creditCardYear = "",
        creditCardCCV = "",
        PATH = "C:\Program Files (x86)\chromedriver.exe"
    )

    bot = PS5Bot(**personal_info)
    bot.add_ps5_to_cart_and_checkout()
    bot.filling_shipping_info()
    bot.fill_out_payment_and_order()
    # You can add those methods in the __init__ as well

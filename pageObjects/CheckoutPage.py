from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements(By.CSS_SELECTOR, ".card-title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    addToCart = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH,"//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getaddToCart(self):
        return self.driver.find_element(*CheckOutPage.addToCart)

    def getCheckOut(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryName = (By.ID,"country")
    India = (By.LINK_TEXT,"India")
    checkBox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    Submit = (By.CSS_SELECTOR,"[type='submit']")
    successMsg = (By.CSS_SELECTOR,"[class*='alert-success']")

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def getIndia(self):
        return self.driver.find_element(*ConfirmPage.India)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.Submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg)
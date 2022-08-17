from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        #HomePage.py
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()

        log.info("Getting all the card titles")

        cards = checkoutpage.getCardTitles()  #CheckoutPage.py
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.getaddToCart().click()

        confirmpage = checkoutpage.getCheckOut()
        log.info("Entering Country name as ind")

        #ConfirmPage.py
        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCountryName().send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        confirmPage.getIndia().click()
        confirmPage.getCheckBox().click()
        confirmPage.getSubmit().click()
        alertText = confirmPage.getSuccessMsg().text
        log.info("Text received from application is" + alertText)

        assert ("Success! Thdfgank you!" in alertText)




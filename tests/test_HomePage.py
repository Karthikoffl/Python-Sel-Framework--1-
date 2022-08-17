import pytest
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionsByText(homepage.getGender(), getData["gender"]) #Base class

        homepage.submitForm().click()

        alertText = homepage.getSuccessMsg().text

        assert ("Success" in alertText)
        self.driver.refresh()


    @pytest.fixture(params = HomePageData.getTestData("Testcase2 -> from excel"))
    def getData(self, request):
        return request.param


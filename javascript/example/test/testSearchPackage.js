const { By, Builder } = require("selenium-webdriver");
const { WebPage } = require("citronella");
const ContentsPage = require("../page/contents-page");
const assert = require("assert");

describe("test search package", function () {
  this.timeout(10000);
  before(async function () {
    driver = await new Builder().forBrowser("chrome").build();
    web = new WebPage(driver, 10000, true);
    web.page = ContentsPage;
    await web.driver.get("https://www.npmjs.com/");
  });

  after(async function () {
    driver.quit();
  });

  it("results list include citronella", async function () {
    await web.page.homePage.searchPackagesInput.sendKeys("citron");
    await web.page.homePage.searchButton.click();
    let ElementsResult =
      await web.page.searchPage.searchResultLists.getElements();
    let textList = [];
    for (let i in ElementsResult) {
      textList.push(await ElementsResult[i].getText());
    }
    assert.match(textList.join(), /citronella/);
  });
});

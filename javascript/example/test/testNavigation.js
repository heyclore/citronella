const { By, Builder} = require('selenium-webdriver');
const { WebPage } = require('citronella')
const ContentsPage = require('../page/contents-page')
const assert = require('assert');


describe('test navigation', function () {
  this.timeout(10000);
  before(async function () {
    driver = await new Builder().forBrowser('chrome').build();
    web = new WebPage(driver, 10000, true);
    await web.pageObject(new ContentsPage().homePage);
    await web.driver.get('https://www.npmjs.com/')
  });

  after(async function () {
    driver.quit()
  });

  it('navigate to a pro page', async function () {
    await web.page.proButton.click()
    title = await web.driver.getTitle()
    await assert.match(title, /Pro/)
  });

  it('navigate to a teams page', async function () {
    await web.page.teamsButton.click()
    title = await web.driver.getTitle()
    await assert.match(title, /Teams/)
  });

  it('navigate to a products page', async function () {
    await web.page.pricingButton.click()
    title = await web.driver.getTitle()
    await assert.match(title, /Products/)
  });

  it('navigate to a home page', async function () {
    await web.page.npmHomepageIcon.click()
    title = await web.driver.getTitle()
    await assert.match(title, /npm/)
  });
});
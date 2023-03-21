const { By, Builder} = require('selenium-webdriver');
const { ui, WebPage, PlaceholderPage } = require('citronella')
const ContentsPage = require('../example/page/contents-page')

async function page()
{
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver, 10000, true);
  await web.pageObject(new ContentsPage().homePage);
  await web.driver.get('https://www.npmjs.com/')
  await web.page.searchPackagesInput.sendKeys('selenium')
  await web.page.searchButton.click()
  let ElementsResult = await web.page.searchResultLists.getElements()
  let textList = []
  for (let i in ElementsResult) {
    textList.push(await ElementsResult[i].getText())
  }
  console.log(textList)
  await web.driver.get('https://www.npmjs.com/package/citronella')
  await web.back
  web.driver.quit()
}

async function locator()
{
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver, 10000, true);
  await web.pageObject(new ContentsPage().homePage, url=true);
  await web.readyState()
  await web.locate(By.name('q')).sendKeys('selenium')
  await web.locate(By.css('button[type="submit"]')).click()
  await web.back
  web.driver.quit()
}

async function webUi()
{
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver, 10000, true);
  await web.pageObject(new ContentsPage().homePage, url=true);
  await web.page.searchPackagesInput.untilElementLocated()
  await web.page.searchPackagesInput.untilElementsLocated()
  await web.page.searchPackagesInput.untilElementIsVisible()
  //await web.page.searchPackagesInput.untilElementIsNotVisible()
  await web.page.searchPackagesInput.untilElementIsEnabled()
  //await web.page.searchPackagesInput.untilElementIsDisabled()
  //await web.page.searchPackagesInput.untilElementIsSelected()
  await web.page.searchPackagesInput.untilElementIsNotSelected()
  web.driver.quit()
}

async function key()
{
  let driver = await new Builder().forBrowser('chrome').build();
  //let driver = await new WebdriverDummy()
  let web = new WebPage(driver, 10000, true);
  await web.pageObject(new ContentsPage().homePage);
  await web.driver.get('https://www.npmjs.com/')
  await web.page.searchPackagesInput.sendKeys('selenium', {enter: true})
  let ElementsResult = await web.page.searchResultLists.getElements()
  let textList = []
  for (let i in ElementsResult) {
    textList.push(await ElementsResult[i].getText())
  }
  console.log(textList)
  await web.driver.quit()
}

page()
//locator()
//webUi()
//key()

const { By, Builder} = require('selenium-webdriver');
const { ui, WebPage } = require('citronella')
const ContentsPage = require('../example/page/contents-page')

class Webb{
  get(x){return this;}
  wait(x){return this;}
  sendKeys(x){return this;}
  click(x){return this;}
  navigate(x){return this;}
  back(x){return this;}
  quit(x){return this;}
}

async function page()
{
  let driver = await new Builder().forBrowser('chrome').build();
  //let driver = new Webb();
  let web = new WebPage(driver, 10000, true);
  web.page = ContentsPage;
  await web.driver.get('https://www.npmjs.com/')
  await web.page.homePage.searchPackagesInput.sendKeys('selenium')
  await web.page.homePage.searchButton.click()
  let ElementsResult = await web.page.searchPage.searchResultLists.getElements()
  let textList = []
  for (let i in ElementsResult) {
    textList.push(await ElementsResult[i].getText())
  }
  console.log(textList)
  await web.driver.get('https://www.npmjs.com/package/citronella')
  web.driver.quit()
}

async function locator()
{
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver, 10000, true);
  await web.driver.get('https://www.npmjs.com/')
  await web.readyState()
  await web.locate(By.name('q')).sendKeys('selenium')
  await web.locate(By.css('button[type="submit"]')).click()
  web.driver.quit()
}

async function webUi()
{
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver, 10000, true);
  web.page = ContentsPage;
  await web.driver.get('https://www.npmjs.com/')
  await web.page.homePage.searchPackagesInput.untilElementLocated()
  await web.page.homePage.searchPackagesInput.untilElementsLocated()
  await web.page.homePage.searchPackagesInput.untilElementIsVisible()
  //await web.page.homePage.searchPackagesInput.untilElementIsNotVisible()
  await web.page.homePage.searchPackagesInput.untilElementIsEnabled()
  //await web.page.homePage.searchPackagesInput.untilElementIsDisabled()
  //await web.page.homePage.searchPackagesInput.untilElementIsSelected()
  await web.page.homePage.searchPackagesInput.untilElementIsNotSelected()
  web.driver.quit()
}

async function key()
{
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver, 10000, true);
  web.page = ContentsPage;
  await web.driver.get('https://www.npmjs.com/')
  await web.page.homePage.searchPackagesInput.sendKeys('selenium', {enter: true})
  let ElementsResult = await web.page.searchPage.searchResultLists.getElements()
  let textList = []
  for (let i in ElementsResult) {
    textList.push(await ElementsResult[i].getText())
  }
  console.log(textList)
  await web.driver.quit()
}

async function main()
{
  await page()
  await locator()
  await webUi()
  await key()
}
main()

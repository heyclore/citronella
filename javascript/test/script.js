const { By, Builder } = require('selenium-webdriver');
const { ui, WebPage } = require('../index')

class WebdriverDummy
{
  get (x){return 1}
  wait (x){return this}
  sendKeys (x){return 1}
  click (x){return 1}
  getText(){return [11,2,3]}
}

class Foobar
{
  get searchPackagesInput2()
  {
    return ui(By.name('q'));
  }
}

class HomePage extends Foobar
{
  get searchPackagesInput()
  {
    return ui(By.name('q'));
  }
  get searchButton()
  {
    return ui(By.css('button[type="submit"]'), SearchPage);
  }
}

class SearchPage
{
  get searchResultLists()
  {
    return ui(By.css('a[target="_self"]'));
  }
}

async function example()
{
  let driver = await new Builder().forBrowser('chrome').build();
  //let driver = await new WebdriverDummy()
  let web = new WebPage(driver);
  web.pageObject(HomePage);
  await driver.get('https://www.npmjs.com/')
  await web.page.searchPackagesInput.sendKeys('selenium')
  await web.page.searchButton.click()
  let ElementsResult = await web.page.searchResultLists.getElements()
  let textList = []
  for (let i in ElementsResult) {
    textList.push(await ElementsResult[i].getText())
  }
  console.log(textList)
  web.driver.quit()
}

example()

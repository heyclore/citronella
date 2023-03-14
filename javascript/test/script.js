const { By, Builder } = require('selenium-webdriver');
const { ui, WebPage } = require('../lib/index')

class WebdriverDummy
{
  get (x){return 1}
  wait (x){return this}
  sendKeys (x){return 1}
  click (x){return 1}
  getText(){return [11,2,3]}
  quit(){}
  navigate(){return this}
  back(){}
}

class ContentsPage
{
  get fooBar(){
    return Foobar
  }

  get homePage(){
    return HomePage
  }

  get searchPage(){
    return SearchPage
  }
}

class Foobar
{
  get searchPackagesInput2()
  {
    return ui(By.name('q'));
  }
}

class HomePage extends new ContentsPage().fooBar
{
  static URL = 'https://www.npmjs.com/'
  get searchPackagesInput()
  {
    return ui(By.name('q'));
  }
  get searchButton()
  {
    return ui(By.css('button[type="submit"]'), new ContentsPage().searchPage);
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
  await web.pageObject(new ContentsPage().homePage, url=true);
  //await driver.get('https://www.npmjs.com/')
  await web.page.searchPackagesInput.sendKeys('selenium')
  web.webdriverWait(66666666)
  await web.page.searchButton.click()
  let ElementsResult = await web.page.searchResultLists.getElements()
  let textList = []
  for (let i in ElementsResult) {
    textList.push(await ElementsResult[i].getText())
  }
  console.log(textList)
  web.back
  web.driver.quit()
}

example()

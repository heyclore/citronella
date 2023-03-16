const { By, Builder } = require('selenium-webdriver');
const { ui, WebPage, PlaceholderPage } = require('../lib/index')

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

  get github_icon_link()
  {
    return ui(By.css('div.w-100 a.ph3'), new PlaceholderPage)
  }
}
async function test2()
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

async function test()
{
  let driver = await new Builder().forBrowser('chrome').build();
  //let driver = await new WebdriverDummy()
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
  await web.page.github_icon_link.click()
  await web.back
  await web.driver.quit()
}

test()
//test2()

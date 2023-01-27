const {By, until, Builder} = require('selenium-webdriver');

function logWrapper(className, functionName, func) {
  return function() {
    console.log(className +' => '+ functionName +' => ' + func.name);
    let result = func.apply(this, arguments);
    //console.log("Function result: ", result);
    return result;
  };
}

function pageDecorator(cls, driver, pageLists, webdriverWait)
{
  let page =  new cls();
  let originalGetters = {};
  let propertyNames = Object.getOwnPropertyNames(Object.getPrototypeOf(page));

  //for (let i = 0; i < propertyNames.length; i++) {
  for (let i in propertyNames) {
    let propertyName = propertyNames[i];
    let property = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(page), propertyName);
    //console.log(property)
    if (property.get) {
      //console.log(property.get)
      originalGetters[propertyName] = property.get;
      Object.defineProperty(page, propertyName, {
        get: function () {
          let obj = originalGetters[propertyName].call(this);
          let element = new Ui(driver, obj.by, obj.page, pageLists, webdriverWait)
          element.click = logWrapper(page.constructor.name, propertyName, element.click);
          element.sendKeys = logWrapper(page.constructor.name, propertyName, element.sendKeys);
          element.getElements = logWrapper(page.constructor.name, propertyName, element.getElements);
          return element
        }
      });
    }
  }
  return page
}

class WebPage
{
  constructor(driver, wait=10000)
  {
    this.driver = driver;
    this.webdriverWait = wait;
    this.pageLists = [];
  }
  pageObject(x)
  {
    this.pageLists.unshift(x)
  }
  get page()
  {
    //let page =  new this.pageLists[0]();
    //pageDecorator(page, this.driver, this.pageLists, page.constructor.name, this.webdriverWait)
    //return page;
    return pageDecorator(this.pageLists[0], this.driver, this.pageLists, this.webdriverWait)
  }
}

class Ui
{
  constructor(driver, by, page, pageLists, wait)
  {
    this.driver = driver;
    this.locator = by;
    this.page = page;
    this.pageLists = pageLists;
    this.wait = wait;
  }

  async click()
  {
    let el = await this.driver.wait(until.elementLocated(this.locator),15000);
    await el.click()
    this.pageLists.unshift(this.page)
    //console.log(this)
    if(this.pageLists.length >= 5)
    {
      this.pageLists.pop()
    }
  }
  async sendKeys(x)
  {
    let el = await this.driver.wait(until.elementLocated(this.locator),15000);
    await el.sendKeys(x)
  }
  async getElements()
  {
    let el = await this.driver.wait(until.elementsLocated(this.locator),15000);
    return el
  }
}

function ui(by, page){
  return {
    'by': by,
    'page': page,
  }
}

class Foobar
{
  get foo()
  {
    console.log('foo')
    return ui(By.xpath('fooo'), HomePage);
  }
}

class HomePage
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

class WebdriverDummy
{
  get (x){return 1}
  wait (x){return this}
  sendKeys (x){return 1}
  click (x){return 1}
  getText(){return [11,2,3]}
}


async function example()
{
  //let driver = await new WebdriverDummy()
  let driver = await new Builder().forBrowser('chrome').build();
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
}

example()

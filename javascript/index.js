const webdriver = require('selenium-webdriver');


var until = webdriver.until;
var By = webdriver.By;

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
    if (property.get) {
      originalGetters[propertyName] = property.get;
      Object.defineProperty(page, propertyName, {
        get: function () {
          let obj = originalGetters[propertyName].call(this);
          obj.driver = driver
          obj.pageLists = pageLists
          //obj.functionName = propertyName
          //obj.className = page.constructor.name
          obj.wait = webdriverWait
          obj.click = logWrapper(page.constructor.name, propertyName, obj.click);
          return obj;
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
  constructor(by, page)
  {
    this.locator = by;
    this.page = page;
    this.driver = null;
    this.pageLists = null;
    //this.functionName = null;
    //this.className = null;
    this.wait = null;
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
}


class HomePage
{
  get helpMenuButton()
  {
    return new Ui(By.xpath('//li[@class="horizontal-menu__item"][1]'), HelpPage);
  }
}

class HelpPage
{
  get homeMenuButton()
  {
    return new Ui(By.className('site-header__logo'), HomePage);
  }
}





async function example()
{
  let driver = await new webdriver.Builder().forBrowser('chrome').build();
  let web = new WebPage(driver);
  web.pageObject(HomePage);
  await driver.get('https://pypi.org/')
  await web.page.helpMenuButton.click()
  await web.page.homeMenuButton.click()
  await web.page.helpMenuButton.click()
  await web.page.homeMenuButton.click()
}

example()

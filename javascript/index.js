const {By, until, Builder} = require('selenium-webdriver');

function logWrapper(className, functionName, func)
{
  return function()
  {
    console.log(className +' => '+ functionName +' => ' + func.name);
    let result = func.apply(this, arguments);
    //console.log("Function result: ", result);
    return result;
  };
}

function pageDecorator(cls, driver, pageLists, webdriverWait)
{
  page = new cls();

  function listPropertiesRecursive(x)
  {
    let proto = Object.getPrototypeOf(x);
    if (proto !== null)
    {
      let propertyNames = Object.getOwnPropertyNames(proto);
      let originalGetters = {};

      for (let i in propertyNames)
      {
        let propertyName = propertyNames[i];
        let property = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(x), propertyName);
        if (property.get)
        {
          originalGetters[propertyName] = property.get;

          if (property.get.name == 'get __proto__')
          {
            return
          } else if(property.get().click)
          {
            return
          }

          Object.defineProperty(x, propertyName, {
            get: function ()
            {
              let obj = originalGetters[propertyName].call(this);
              let ui = new Ui(driver, obj.by, obj.page, pageLists, webdriverWait)
              ui.click = logWrapper(page.constructor.name, propertyName, ui.click);
              ui.sendKeys = logWrapper(page.constructor.name, propertyName, ui.sendKeys);
              ui.getElements = logWrapper(page.constructor.name, propertyName, ui.getElements);
              ui.propertyName = logWrapper(page.constructor.name, propertyName, ui.getElements);
              return ui
            }
          });
        }
      }

      listPropertiesRecursive(proto);
    }
  }

  listPropertiesRecursive(page)
  return page
}


class WebPage
{
  #driver;
  #webdriverWait;
  #pageLists;

  constructor(driver, wait=10000)
  {
    this.#driver = driver;
    this.#webdriverWait = wait;
    this.#pageLists = [];
  }

  pageObject(x)
  {
    this.#pageLists.unshift(x)
  }

  get driver()
  {
    return this.#driver
  }

  get page()
  {
    return pageDecorator(this.#pageLists[0], this.#driver, this.#pageLists, this.#webdriverWait)
  }
}

class Ui
{
  #driver;
  #locator;
  #page;
  #pageLists;
  #wait;

  constructor(driver, by, page, pageLists, wait)
  {
    this.#driver = driver;
    this.#locator = by;
    this.#page = page;
    this.#pageLists = pageLists;
    this.#wait = wait;
  }

  async click()
  {
    let el = await this.#driver.wait(until.elementLocated(this.#locator),15000);
    await el.click()
    this.#pageLists.unshift(this.#page)
    //console.log(this)
    if(this.#pageLists.length >= 5)
    {
      this.#pageLists.pop()
    }
  }

  async sendKeys(x)
  {
    let el = await this.#driver.wait(until.elementLocated(this.#locator),15000);
    await el.sendKeys(x)
  }

  async getElements()
  {
    return await this.#driver.wait(until.elementsLocated(this.#locator),15000);
  }
}

function ui(by, page)
{
  return {
    'by': by,
    'page': page,
  }
}

class SearchComponents
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

class HomePage extends SearchComponents
{

  get homeHeadline()
  {
    return ui(By.className('f-subheadline-m'));
  }
}

class SearchPage extends SearchComponents
{

  get searchResultLists()
  {
    return ui(By.css('a[target="_self"]'));
  }
}

class SimulateWebdriver
{
  get (x){return 1}
  wait (x){return this}
  sendKeys (x){return 1}
  click (x){return 1}
}

async function example()
{
  //let driver = new SimulateWebdriver()
  let driver = await new Builder().forBrowser('chrome').build();
  let web = new WebPage(driver);
  web.pageObject(HomePage);
  await web.driver.get('https://www.npmjs.com/')
  await web.page.searchPackagesInput.sendKeys('selenium')
  await web.page.searchButton.click()
  let elementsResult = await web.page.searchResultLists.getElements()
  let textList = []
  for (let i in elementsResult) {
    textList.push(await elementsResult[i].getText())
  }
  console.log(textList)

}

example()

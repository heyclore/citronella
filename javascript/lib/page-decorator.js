'use strict'

const { until } = require('selenium-webdriver');
const logWrapper = require('./log-wrapper')

class WebUi
{
  #driver;
  #locator;
  #page;
  #pageLists;
  #wait;
  #logger;

  constructor(driver, by, page, pageLists, wait, logger)
  {
    this.#driver = driver;
    this.#locator = by;
    this.#page = page;
    this.#pageLists = pageLists;
    this.#wait = wait;
    this.#logger = logger;
    console.log(wait)
  }

  async click()
  {
    let el = await this.#driver.wait(until.elementLocated(this.#locator),this.#wait);
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
    let el = await this.#driver.wait(until.elementLocated(this.#locator),this.#wait);
    await el.sendKeys(x)
  }

  async getElements()
  {
    return await this.#driver.wait(until.elementsLocated(this.#locator),this.#wait);
  }
}

function pageDecorator(driver, webdriverWait, pageLists, logger)
{
  let page = new pageLists.currentPage();

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

          if (property.get.name == 'get __proto__' || property.get().click )
          {
            return
          }

          Object.defineProperty(x, propertyName, {
            get: function ()
            {
              let obj = originalGetters[propertyName].call(this);
              let ui = new WebUi(driver, obj.by, obj.page, pageLists, webdriverWait, logger)
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

module.exports = pageDecorator;

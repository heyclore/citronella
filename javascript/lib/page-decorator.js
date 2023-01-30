'use strict'

const { until } = require('selenium-webdriver');
const logWrapper = require('./log-wrapper')

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

function pageDecorator(cls, driver, pageLists, webdriverWait)
{
  let page = new cls();

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

module.exports = pageDecorator;

'use strict'

const pageDecorator = require('./page-decorator')

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

module.exports = WebPage

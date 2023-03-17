'use strict'

const { until } = require('selenium-webdriver');
const PageDecorator = require('./page-decorator')
const PageTab = require('./page-tab')
const WebUi = require('./web-ui')

class WebPage{
  #driver;
  #wait;
  #pageLists;
  #logger;

  constructor(driver, wait, logger){
    this.#driver = driver;
    this.#wait = wait;
    this.#pageLists = new PageTab;
    this.#logger = logger
  }

  get driver(){
    return this.#driver
  }

  get page(){
    return new PageDecorator({driver:this.#driver, webdriverWait:this.#wait, pageLists:this.#pageLists, logger:this.#logger})
  }

  pageObject(newPage, url=false){
    this.#pageLists.unshift(newPage)
    if (url){
      let path = newPage.URL
      if(!path){
        throw new Error(`the 'static URL' variable doesn't exist in ${newPage.name}`);
      }
      this.#driver.get(newPage.URL)
    }
  }

  get back(){
    this.#driver.navigate().back()
    this.#pageLists.shift
  }

  locate(by){
  return new WebUi(this.#driver, this.#wait, this.#pageLists, by, null, {logger:false})
  }

  readyState(timeout=10000){
    this.driver.wait(this.driver.executeScript('return document.readyState === "complete";'), timeout)
  }
}

module.exports = WebPage

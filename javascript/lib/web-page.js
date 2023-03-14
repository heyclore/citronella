'use strict'

const pageDecorator = require('./page-decorator')
const PageTab = require('./page-tab')

class WebPage{
  #driver;
  #wait;
  #pageLists;
  #logger;

  constructor(driver, wait=10000, logger=false){
    this.#driver = driver;
    this.#wait = wait;
    this.#pageLists = new PageTab;
    this.#logger = logger
  }

  get driver(){
    return this.#driver
  }

  get page(){
    return pageDecorator(this.#driver, this.#wait, this.#pageLists, this.#logger)
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

  webdriverWait(wait){
    this.#wait = wait
  }
}

module.exports = WebPage

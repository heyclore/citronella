// MIT License
// 
// Copyright (c) 2023 Eko Purnomo
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

'use strict'

const { until } = require('selenium-webdriver');
const PageDecorator = require('./page-decorator')
const WebUi = require('./web-ui')

class WebPage{
  #driver;
  #wait;
  #page;
  #logger;

  constructor(driver, wait, logger){
    this.#driver = driver;
    this.#wait = wait;
    this.#logger = logger
  }

  get driver(){
    return this.#driver
  }

  set page(page){
    this.#page = page
  }

  get page(){
    return new PageDecorator({driver:this.#driver, webdriverWait:this.#wait,
      page:this.#page, logger:this.#logger})
  }

  locate(by){
  return new WebUi(this.#driver, this.#wait, this.#page, by, null, {logger:false})
  }

  readyState(timeout=10000){
    this.driver.wait(this.driver.executeScript('return document.readyState === "complete";'), timeout)
  }
}

module.exports = WebPage

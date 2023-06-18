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

const WebUi = require('./web-ui')

class PageDecorator {
  constructor(driver, wait, page, logger) {
    return new Proxy(this, {
      get(target, prop) {
        let currentPage = new page()
        if(prop in currentPage){
          let obj = currentPage[prop]
          if(obj.by){
            let ui =  new WebUi(driver, wait, obj.by,
              {logger: logger, cls: currentPage.constructor.name, method: prop})
            return ui
          }
          return new PageDecorator(driver, wait, obj, logger)
        }
        throw new Error(`'${prop}' doesn't exist in '${currentPage.constructor.name}'`);
      }
    });
  }
}

module.exports = PageDecorator;

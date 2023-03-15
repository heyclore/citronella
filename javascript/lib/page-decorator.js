'use strict'

const logWrapper = require('./log-wrapper')
const WebUi = require('./web-ui')


class PageDecorator {
  constructor(args) {
    return new Proxy(this, {
      get(target, prop) {
        let currentPage = new args.pageLists.currentPage()
        if(prop in currentPage){
          let obj = currentPage[prop]
          let ui =  new WebUi(args.driver, args.webdriverWait, args.pageLists, obj.by, obj.page)
          if(args.logger){
            ui.click = logWrapper(currentPage.constructor.name, prop, ui.click);
            ui.sendKeys = logWrapper(currentPage.constructor.name, prop, ui.sendKeys);
            ui.getElements = logWrapper(currentPage.constructor.name, prop, ui.getElements);
            ui.propertyName = logWrapper(currentPage.constructor.name, prop, ui.getElements);
          }
          return ui
        }
        throw new Error(`'${prop}' doesn't exist in '${currentPage.constructor.name}'`);
      }
    });
  }
}


module.exports = PageDecorator;

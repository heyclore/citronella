'use strict'

class PageTab{
  #pageList = [];

  get currentPage(){
    return this.#pageList[0]

  }

  unshift(newPage){
    this.#pageList.unshift(newPage)
  }

  get shift(){
    this.#pageList.shift()
  }

}

module.exports = PageTab

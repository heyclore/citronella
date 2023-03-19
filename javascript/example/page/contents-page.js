class ContentsPage{
  get menuBar(){
    return require('./components/menu-bar')
  }

  get homePage(){
    return require('./home/home-page')
  }

  get proPage(){
    return require('./products/pro/pro-page')
  }

  get teamsPage(){
    return require('./products/teams/teams-page')
  }

  get productsPage(){
    return require('./products/products-page')
  }

  get signupPage(){
    return require('./signup/signup-page')
  }

  get loginPage(){
    return require('./login/login-page')
  }

  get searchPage(){
    return require('./search/search-page')
  }
}

module.exports = ContentsPage

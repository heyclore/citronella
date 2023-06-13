const HomePage =  require('./home/home-page')
const ProPage = require('./products/pro/pro-page')
const TeamsPage = require('./products/teams/teams-page')
const ProductsPage = require('./products/products-page')
const SignupPage = require('./signup/signup-page')
const LoginPage = require('./login/login-page')
const SearchPage = require('./search/search-page')

class ContentsPage{

  get homePage(){
    return HomePage
  }

  get proPage(){
    return ProPage
  }

  get teamsPage(){
    return TeamsPage
  }

  get productsPage(){
    return ProductsPage
  }

  get signupPage(){
    return SignupPage
  }

  get loginPage(){
    return LoginPage
  }

  get searchPage(){
    return SearchPage
  }
}

module.exports = ContentsPage

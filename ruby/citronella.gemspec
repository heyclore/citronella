Gem::Specification.new do |s|
  s.name = 'citronella'
  s.version = '0.0.3'

  s.authors = ['heyclore']
  s.email = 'cloore@gmail.com'

  s.summary = 'Webdriver extension with a page object wrapper'
  s.description = <<-DESCRIPTION
    Webdriver extension with a page object wrapper
  DESCRIPTION

  s.licenses = 'MIT'
  s.required_ruby_version = '>= 2.7.0'
  s.homepage = 'https://github.com/heyclore/citronella#readme'
  s.metadata = {
    'source_code_uri' => 'https://github.com/heyclore/citronella/tree/main/ruby',
    'github_repo' => 'https://github.com/heyclore/citronella',
  }

  s.files = ['README.md', 'Gemfile', 'citronella.gemspec']
  s.files += Dir['lib/**/*.rb']

  s.add_runtime_dependency 'selenium-webdriver', ['~> 4.8']
end

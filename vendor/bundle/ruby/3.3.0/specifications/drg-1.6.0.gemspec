# -*- encoding: utf-8 -*-
# stub: drg 1.6.0 ruby lib

Gem::Specification.new do |s|
  s.name = "drg".freeze
  s.version = "1.6.0".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Ryan Buckley".freeze]
  s.date = "2020-02-03"
  s.description = "DRG that Gemfile! The missing bundler extension. Gem version automation with Bundler".freeze
  s.email = ["arebuckley@gmail.com".freeze]
  s.homepage = "https://github.com/ridiculous/drg".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.0.6".freeze
  s.summary = "DRG that Gemfile! The missing bundler extension".freeze

  s.installed_by_version = "3.6.3".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<bundler>.freeze, [">= 1.10".freeze, "< 3.0".freeze])
  s.add_runtime_dependency(%q<highline>.freeze, [">= 1.6".freeze, "< 3.0".freeze])
  s.add_development_dependency(%q<rake>.freeze, ["~> 10.0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, [">= 3.2".freeze, "< 4".freeze])
end

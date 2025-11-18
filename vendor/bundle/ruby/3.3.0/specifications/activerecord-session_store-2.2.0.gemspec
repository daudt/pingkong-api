# -*- encoding: utf-8 -*-
# stub: activerecord-session_store 2.2.0 ruby lib

Gem::Specification.new do |s|
  s.name = "activerecord-session_store".freeze
  s.version = "2.2.0".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "changelog_uri" => "https://github.com/rails/activerecord-session_store/blob/master/CHANGELOG.md", "homepage_uri" => "https://github.com/rails/activerecord-session_store", "source_code_uri" => "https://github.com/rails/activerecord-session_store" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["David Heinemeier Hansson".freeze]
  s.date = "2025-03-26"
  s.email = "david@loudthinking.com".freeze
  s.extra_rdoc_files = ["README.md".freeze]
  s.files = ["README.md".freeze]
  s.homepage = "https://github.com/rails/activerecord-session_store".freeze
  s.licenses = ["MIT".freeze]
  s.rdoc_options = ["--main".freeze, "README.md".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.5.0".freeze)
  s.rubygems_version = "3.6.2".freeze
  s.summary = "An Action Dispatch session store backed by an Active Record class.".freeze

  s.installed_by_version = "3.6.3".freeze

  s.specification_version = 4

  s.add_runtime_dependency(%q<activerecord>.freeze, [">= 7.0".freeze])
  s.add_runtime_dependency(%q<actionpack>.freeze, [">= 7.0".freeze])
  s.add_runtime_dependency(%q<railties>.freeze, [">= 7.0".freeze])
  s.add_runtime_dependency(%q<rack>.freeze, [">= 2.0.8".freeze, "< 4".freeze])
  s.add_runtime_dependency(%q<cgi>.freeze, [">= 0.3.6".freeze])
end

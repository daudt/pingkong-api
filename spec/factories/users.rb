FactoryGirl.define do

  factory(:user) do |u|
    u.name { Faker::Name.name }
    u.email { Faker::Internet.email }
    u.password { Faker::Internet.password(8) }
    u.nickname { Faker::Name.name }
  end

end
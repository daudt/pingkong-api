class Match < ApplicationRecord
  has_and_belongs_to_many :users
  has_one :winner



end

class User < ApplicationRecord
  has_many :rankings
  has_and_belongs_to_many :matches
  has_many :winners

  # Include default devise modules.
  devise :database_authenticatable, :registerable,
          :recoverable, :rememberable, :trackable, :validatable,
          :confirmable, :omniauthable
  include DeviseTokenAuth::Concerns::User
end

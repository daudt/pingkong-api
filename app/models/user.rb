class User < ApplicationRecord
  has_many :rankings, dependent: :destroy
  has_and_belongs_to_many :matches
  has_many :winners, dependent: :destroy

  before_create :set_rating

  # Include default devise modules.
  devise :database_authenticatable, :registerable,
          :recoverable, :rememberable, :trackable, :validatable,
          :omniauthable

  include DeviseTokenAuth::Concerns::User

  def set_rating
    self.rankings.new(rating: self.rating)
  end

end

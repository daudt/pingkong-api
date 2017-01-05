class Match < ApplicationRecord
  has_and_belongs_to_many :users
  has_one :winner

  before_create :set_uuid

  def set_uuid
    self.uuid = SecureRandom.uuid
  end

end

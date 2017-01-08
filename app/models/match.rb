class Match < ApplicationRecord
  has_and_belongs_to_many :users
  has_one :winner

  before_create :set_uuid

  def set_uuid
    self.uuid = SecureRandom.uuid
  end

  def winning_user
    self.winner.user
  end

  def losing_user
    self.winner.user_id == self.users.first.id ? self.users.second : self.users.first
  end

end

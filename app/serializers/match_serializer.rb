class MatchSerializer < ActiveModel::Serializer
  attributes :match_id, :player1, :player2, :winner, :created_at, :updated_at

  def match_id
    object.id
  end

  def player1
    object.users.first
  end

  def player2
    object.users.last
  end

  def winner
    object.winner.user
  end

end

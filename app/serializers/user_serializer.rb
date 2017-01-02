class UserSerializer < ActiveModel::Serializer
  attributes :id, :name, :email, :nickname, :image, :rating, :num_wins, :num_matches, :num_losses

  def num_matches
    object.matches.count
  end

  def num_wins
    object.winners.count
  end

  def num_losses
    num_matches - num_wins
  end

end

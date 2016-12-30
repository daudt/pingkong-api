class RankingSerializer < ActiveModel::Serializer
  attributes :user_id, :name, :nickname, :rating, :created_at

  def name
    User.find(object.user_id).name
  end

  def nickname
    User.find(object.user_id).nickname
  end

end

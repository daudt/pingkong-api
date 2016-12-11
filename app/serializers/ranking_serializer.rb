class RankingSerializer < ActiveModel::Serializer
  attributes :user_id, :name, :email, :nickname, :rating, :created_at

  def name
    User.find(object.user_id).name
  end

  def email
    User.find(object.user_id).email
  end

  def nickname
    User.find(object.user_id).nickname
  end

end

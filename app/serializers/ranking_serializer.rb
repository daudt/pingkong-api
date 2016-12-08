class RankingSerializer < ActiveModel::Serializer
  attributes :id, :user_id, :rating, :created_at
end

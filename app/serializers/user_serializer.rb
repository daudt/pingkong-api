class UserSerializer < ActiveModel::Serializer
  attributes :id, :name, :email, :nickname, :image, :rating
end

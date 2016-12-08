class ChangeDefaultRating < ActiveRecord::Migration[5.0]
  def change
    change_column :users, :rating, :integer, default: 1000
  end
end

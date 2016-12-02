class AddRatingToUsers < ActiveRecord::Migration[5.0]
  def change
    change_table :users do |t|
      t.integer :rating, default: 0
    end

  end
end

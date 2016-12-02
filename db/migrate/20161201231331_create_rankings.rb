class CreateRankings < ActiveRecord::Migration[5.0]
  def change
    create_table :rankings do |t|
      t.integer :rating
      t.belongs_to :user, index: true

      t.timestamps
    end
  end
end

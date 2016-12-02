class CreateMatches < ActiveRecord::Migration[5.0]
  def change
    create_table :matches do |t|
      t.timestamps
    end

    create_table :matches_users do |t|
      t.belongs_to :user, index: true
      t.belongs_to :match, index: true
      t.boolean :winner
    end

  end
end

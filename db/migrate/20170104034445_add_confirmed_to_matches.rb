class AddConfirmedToMatches < ActiveRecord::Migration[5.0]
  def up
    add_column :matches, :confirmed, :boolean, default: false, null: false
    Match.find_each do |match|
      match.confirmed = true
      match.save!
    end
  end

  def down
    remove_column :matches, :confirmed
  end
end

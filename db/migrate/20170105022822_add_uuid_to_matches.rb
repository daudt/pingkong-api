class AddUuidToMatches < ActiveRecord::Migration[5.0]
  def change
    add_column :matches, :uuid, :uuid
  end
end

class CreatePeople < ActiveRecord::Migration
  def change
    create_table :people do |t|
      t.string :name
      t.integer :family_id
      t.string :session_id
      t.integer :recipient

      t.timestamps
    end

    create_table :families do |t|
	    t.string :name
	    t.string :session_id
		t.timestamps
  	end

  	#add_foreign_key :people, :families

  end
end

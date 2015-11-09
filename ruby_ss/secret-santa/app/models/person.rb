class Person < ActiveRecord::Base
	belongs_to :family

	def gifter_string
		puts "Recipient" + self.recipient.to_s
		recipient = Person.find(self.recipient)
		str = self.name + " --> " + recipient.name +  " " + Family.find(recipient.family_id).name
	end

end

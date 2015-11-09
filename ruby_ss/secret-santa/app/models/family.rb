class Family < ActiveRecord::Base
    has_many :people

    def self.GenerateRecipients(list_of_people)
        #Person with Family Id
        recursiveSecretSanta(list_of_people)

    end

    def self.recursiveSecretSanta(people_in_session)
        #Base case
        matches = people_in_session.where.not(recipient: nil)
        puts "Non null recipient count: " + matches.count.to_s #Should be 0 to start
        puts "Total people: " + people_in_session.count.to_s #Should be 4 to start

        if matches.count == people_in_session.count
            #puts "BASE CASE GOOD"
            return true 
        end
        #else...Recursive case
        people_in_session.where(recipient: nil).shuffle.each do |gifter|
            #puts "For GIFTER, " +  gifter.name
            possible_giftees = getGiftees(gifter, people_in_session)
            #puts "This many possible giftees: " + possible_giftees.count.to_s
            if possible_giftees.count > 0
                possible_giftees.each do |giftee|
                    #Update the gifter
                    gifter.recipient = giftee.id
                    gifter.save

                    if recursiveSecretSanta(people_in_session)
                        puts "TRUE"
                        return people_in_session
                    else
                        puts "SETTING NIL"
                        gifter.recipient = nil
                        gifter.save
                    end
                end
            else
                puts "FALSE"
                return false #nil #Same as False
            end
        end
    end


    def self.getGiftees(gifter, people_in_session)
        # First get all the people from a different family
        non_family_members = people_in_session.where.not(family_id: gifter.family_id)
        # Get the ids of all recipients (who aren't null), no one gets 2 gifts
        people_already_taken = people_in_session.where.not(recipient: nil).pluck(:recipient)
        #Get a list of all recipients
        puts "Non family members: #{non_family_members.pluck(:id).to_s}"
        puts "People already taken #{people_already_taken.to_s}"

        if people_already_taken.count == 0 then return non_family_members end

        return non_family_members.where("id NOT IN (?)", people_already_taken)
    end

end

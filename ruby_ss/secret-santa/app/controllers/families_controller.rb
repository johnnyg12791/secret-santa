class FamiliesController < ApplicationController
	def index
    	people_in_session = Person.where(session_id: request.session.id) #.order(:family)

    	Family.GenerateRecipients(people_in_session)

    	@families = []
    	people_in_session.each do |p| 
    		if !@families.include? Family.find(p.family_id)
    			@families << Family.find(p.family_id)
    		end
    	end

		render 'families'
	end



	def gifters
		# Get everyone for that specific family
		@family_members = Person.where(family_id: params[:id])
		# Print who them have
		render 'gifters' #redirect_to :action => :gifters


	end



end
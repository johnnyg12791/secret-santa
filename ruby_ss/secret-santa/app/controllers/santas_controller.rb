class SantasController < ApplicationController
  def index
  end
  
  def new
    @people_in_session = Person.where(session_id: request.session.id) #.order(:family)

  end

  #def show
    #@person = Person.find(params[:id])
  #end
  
  def create
    # Get a list of families for the current session id
    families_in_session = Family.where(session_id: request.session.id)
    # See if any of the names are the same
    family_names = families_in_session.pluck(:name)
    puts "Familes in session"
    puts families_in_session.to_s
    
    puts "Family names"
    puts family_names.to_s
    # If they are, get the id, add it into the person
    family = nil
    puts valid_params
    family_name = valid_params[:family_name]
    if family_names.include? family_name
        family = families_in_session.where(name: family_name).take
    # Otherwise add to family table    
    else
        family = Family.new
        family.name = family_name
        family.session_id = request.session.id
        family.save
    end
    puts "Family"
    puts family.to_s

    person = Person.new
    person.name = valid_params[:name]
    person.session_id = request.session.id
    person.family_id = family.id
    person.recipient = nil
    person.save
    
    #@people_in_session = Person.where(session_id: request.session.id) #.order(:family)
    redirect_to :action => :new
  end


  def destroy
    @person_to_delete = Person.find(params[:id])
    @person_to_delete.destroy

    #@people_in_session = Person.where(session_id: request.session.id) #.order(:family)
    redirect_to :action => :new #santas_path '/new'
    #redirect_to :action => :new
  end


  def view
    #Do some things
    render 'families'
  end

  def generate_gifters
    redirect_to :action => :new
  end


  private
  def valid_params
    params.require(:person).permit(:name, :family_name)
  end



end

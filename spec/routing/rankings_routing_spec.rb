require "rails_helper"

RSpec.describe RankingsController, type: :routing do
  describe "routing" do

    it "routes to #index" do
      expect(:get => "/rankings").to route_to("rankings#index")
    end

    it "routes to #new" do
      expect(:get => "/rankings/new").to route_to("rankings#new")
    end

    it "routes to #show" do
      expect(:get => "/rankings/1").to route_to("rankings#show", :id => "1")
    end

    it "routes to #edit" do
      expect(:get => "/rankings/1/edit").to route_to("rankings#edit", :id => "1")
    end

    it "routes to #create" do
      expect(:post => "/rankings").to route_to("rankings#create")
    end

    it "routes to #update via PUT" do
      expect(:put => "/rankings/1").to route_to("rankings#update", :id => "1")
    end

    it "routes to #update via PATCH" do
      expect(:patch => "/rankings/1").to route_to("rankings#update", :id => "1")
    end

    it "routes to #destroy" do
      expect(:delete => "/rankings/1").to route_to("rankings#destroy", :id => "1")
    end

  end
end

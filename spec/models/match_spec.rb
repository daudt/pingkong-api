require 'rails_helper'

describe Match do

  before(:all) do
    @match = FactoryGirl.create(:match)
    @user1 = FactoryGirl.create(:user)
    @user2 = FactoryGirl.create(:user)
    @match.users = [ @user1, @user2 ]
    @match.winner = Winner.new({user: @user2})
  end

  it 'should have one winner' do
    should have_one :winner
  end

  it 'should have and belong to many users' do
    should have_and_belong_to_many :users
  end

  it 'should have an UUID' do
    expect(@match.uuid).to match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/)
  end

  it 'should have winner as user2' do
    expect(@match.winning_user).to equal(@user2)
  end

  it 'should have looser as user1' do
    expect(@match.losing_user).to equal(@user1)
  end

  after(:all) do
    Match.destroy_all
  end


end

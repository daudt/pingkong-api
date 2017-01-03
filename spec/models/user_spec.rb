require 'rails_helper'

describe User do

  before(:all) do
    @attributes = FactoryGirl.attributes_for(:user)
    @player1 = FactoryGirl.create(:user)
  end

  it { should have_many :rankings}
  it { should have_many :winners }
  it { should have_and_belong_to_many :matches }

  it { should allow_value(@attributes[:name]).for(:name) }
  it { should allow_value(@attributes[:email]).for(:email) }
  it { should allow_value(@attributes[:nickname]).for(:nickname) }
  it { should allow_value(@attributes[:password]).for(:password) }
  it { should allow_value(@attributes[:image]).for(:image)}

  it 'should have an UUID' do
    expect(@player1.uuid).to match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/)
  end

  it 'should have a initial rating of 1000' do
    expect(@player1.rating).to equal(1000)
  end

  it 'should have zero matches' do
    expect(@player1.num_matches).to equal(0)
  end

  it 'should have zero wins' do
    expect(@player1.num_wins).to equal(0)
  end

  it 'should have zero losses' do
    expect(@player1.num_losses).to equal(0)
  end

  after(:all) do
    User.destroy_all
  end

end


require 'rails_helper'

describe User do

  before(:all) do
    @attributes = FactoryGirl.attributes_for(:user)
    @user = FactoryGirl.create(:user)
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
    expect(@user.uuid).to match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/)
  end

  it 'should have a initial rating of 1000' do
    expect(@user.rating).to equal(1000)
  end

  it 'should have zero matches' do
    expect(@user.num_matches).to equal(0)
  end

  it 'should have zero wins' do
    expect(@user.num_wins).to equal(0)
  end

  it 'should have zero losses' do
    expect(@user.num_losses).to equal(0)
  end

  after(:all) do
    User.destroy_all
  end

end


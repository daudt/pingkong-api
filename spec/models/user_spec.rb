require 'rails_helper'

describe User do

  before(:all) do
    @attributes = FactoryGirl.attributes_for(:user)
    @user = FactoryGirl.create(:user)
  end

  it 'should have mnay rankings' do
    should have_many :rankings
  end

  it 'should have many winners' do
    should have_many :winners
  end

  it 'should have and belong to many matches' do
    should have_and_belong_to_many :matches
  end

  it 'should allow attribute name' do
    should allow_value(@attributes[:name]).for(:name)
  end

  it 'should allow attribute email' do
    should allow_value(@attributes[:email]).for(:email)
  end

  it 'should allow attribute nickname' do
    should allow_value(@attributes[:nickname]).for(:nickname)
  end

  it 'should allow attribute password' do
    should allow_value(@attributes[:password]).for(:password)
  end

  it 'should allow attribute password confirmation' do
    should allow_value(@attributes[:password_confirmation]).for(:password_confirmation)
  end

  it 'should allow attribute image' do
    should allow_value(@attributes[:image]).for(:image)
  end

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

  it 'should have a preferred name' do
    expect(@user.preferred_name).to equal(@user.nickname)
  end

  it 'should default preferred name to full name if the nickname is missing' do
    user = FactoryGirl.build(:user)
    user.nickname = nil
    expect(user.preferred_name).to equal(user.name)
  end

  after(:all) do
    User.destroy_all
  end

end


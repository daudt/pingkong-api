require 'rails_helper'

RSpec.describe "Rankings", type: :request do
  describe "GET /rankings" do
    it "works! (now write some real specs)" do
      get rankings_path
      expect(response).to have_http_status(200)
    end
  end
end

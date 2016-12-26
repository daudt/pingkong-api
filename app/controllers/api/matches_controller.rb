module Api
  class MatchesController < ApplicationController
    before_action :set_match, only: [:show, :update, :destroy]
    before_action :authenticate_api_user!

    # GET /matches
    def index
      @matches = Match.all
      render json: @matches
    end

    # GET /matches/1
    def show
      render json: @match
    end

    # POST /matches
    def create
      @match = Match.new(match_params)
      player1 = User.find(params[:player1])
      player2 = User.find(params[:player2])
      @match.users = [ player1, player2 ]
      winner = Winner.new
      if player1.id == params[:winner].to_i
        winner.user = player1
      else
        winner.user = player2
      end
      @match.winner = winner
      update_elo(player1, player2, winner.user)
      update_rankings(player1, player2)

      if @match.save
        render json: @match, status: :created, location: api_match_url(@match)
      else
        render json: @match.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /matches/1
    def update
      if @match.update(match_params)
        render json: @match
      else
        render json: @match.errors, status: :unprocessable_entity
      end
    end

    # DELETE /matches/1
    def destroy
      @match.destroy
    end

    private
    # Use callbacks to share common setup or constraints between actions.
    def set_match
      @match = Match.find(params[:id])
    end

    # Only allow a trusted parameter "white list" through.
    def match_params
      params.fetch(:match, {})
    end

    def update_elo(player1, player2, winner)
      player1_elo = Elo::Player.new(rating: player1.rating)
      player2_elo = Elo::Player.new(rating: player2.rating)

      if winner == player1
        player1_elo.wins_from(player2_elo)
      else
        player2_elo.wins_from(player1_elo)
      end

      player1.rating = player1_elo.rating
      player2.rating = player2_elo.rating
      player1.save!
      player2.save!
    end

    def update_rankings(player1, player2)
      player1.rankings << Ranking.create!(rating: player1.rating)
      player2.rankings << Ranking.create!(rating: player2.rating)
    end

  end
end

class MatchesController < ApplicationController
  before_action :set_match, only: [:show, :update, :destroy]

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
    if player1.id == params[:winner]
      winner.user = player1
    else
      winner.user = player2
    end
    @match.winner = winner

    if @match.save
      render json: @match, status: :created, location: @match
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
end

module Api
  class HistoryController < ApplicationController

    def index
      matches = []
      Match.all.order(created_at: :desc).each do |match|
        matches << {
          id:           match.id,
          winner_id:    match.winning_user.id,
          winner_name:  match.winning_user.preferred_name,
          loser_id:     match.losing_user.id,
          loser_name:   match.losing_user.preferred_name,
          is_confirmed: match.confirmed,
          utc:          match.created_at.utc.to_i
        }
      end
      render json: matches
    end

  end
end

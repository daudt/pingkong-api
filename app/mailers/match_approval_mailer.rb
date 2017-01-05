class MatchApprovalMailer < ApplicationMailer

  def match_approval_email(match, recipient, sender, winner)
    @recipient = recipient
    @match = match
    @sender = sender
    @verb = sender == winner ? 'crushed you epically' : 'laid the smack down on you'
    @url = "#{api_matches_url}/#{@match.uuid}/approve"
    mail(to: @recipient.email, subject: 'Please confirm your match')
  end
end

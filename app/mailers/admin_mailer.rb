class AdminMailer < ApplicationMailer

  def new_user_waiting_for_approval(user)
    recipients = User.where(admin: true)
    emails = recipients.collect(&:email).join(',')
    # for test env only
    if Rails.env.test?
      emails = ['admin@kingofpong.com']
    end
    @user = user
    @url = "#{api_users_url}/#{@user.uuid}/approve"
    mail(to: emails, subject: 'New user awaiting approval')
  end

end

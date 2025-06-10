FROM ruby:2.3.3
# Env setup
ENV APP_HOME /kingofpong-api

# Configure apt and deps
RUN apt-get update -qq \
    && apt-get install -y build-essential libpq-dev curl libxml2-dev libxslt1-dev

# for a JS runtime
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \
    && apt-get install -y nodejs

RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ADD . $APP_HOME

RUN bundle install
FROM ruby:2.3.3

RUN apt-get update -qq && apt-get install -y build-essential postgresql-client

WORKDIR /tmp

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

RUN bundle install

RUN mkdir /pingkong-api

ADD . /pingkong-api/

WORKDIR /pingkong-api

RUN bundle exec rake db:migrate

CMD ["rails","server","-b","0.0.0.0"]

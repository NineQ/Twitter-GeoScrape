require 'open-uri'
require 'nokogiri'

domain_url = "https://twitter.com/ARGV[1]"

scrape_page = Nokogiri::HTML(open(domain_url))

def get_tweets(scrape_tweets)
    @data = scrape_tweets.css('p.tweet-text').text
end

def split_data
  @ARGV[1] = @data.split("#quotes")
end

def list_tweets
  @ARGV[1]_tweets[]
end

get_tweets(scrape_page)
split_data
puts list_tweet


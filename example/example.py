from redditbot import RedditBot

class ExampleRedditBot(RedditBot):
	def main(r):
		print('Running example bot')
		#r.do_praw_Reddit_stuff()

if __name__ == '__main__':
    bot = RedditBot()
    bot.run()

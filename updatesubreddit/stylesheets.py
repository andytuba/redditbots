from redditbot import RedditBot
import argparse, glob, sys, itertools
import os
import re

# Derived from https://www.reddit.com/r/reddithax/comments/2nytff/a_python_bot_to_update_your_subreddits_css_in/
class SubredditStylesheetUpdater(RedditBot):
	useragent = 'subreddit-updater-by-u-andytuba'
	app_id = 'DPuHaFaQZcBO6g'
	app_uri = 'https://www.reddit.com/r/RESUpdates/'
	app_scopes = 'modconfig'

	loops = 0

	stylesheets = {
		'example': 'body { background: white; }'
	}

	def __init__(self, filenames):
		super(self.__class__, self).__init__()
		if isinstance(filenames, basestring):
			self.filenames = [ filenames ]
		else:
			self.filenames = filenames

	def main(self, r):
		for filename in self.filenames:
			self.push(filename)

	def push(self, filename):
		#self.log_debug
		print('Handling %s' % filename)
		subreddit_name = os.path.splitext(os.path.basename(filename))[0]
		contents = file_get_contents(filename)

		#self.log_debug
		print("/r/%s will be updated with: \n%s" % (subreddit_name, contents))

		if self.stylesheets.get(subreddit_name) != contents:
			#self.log_info
			print('/r/%s/about/stylesheet is updating...' % (subreddit_name))
			r.set_stylesheet(subreddit_name, contents)
			self.stylesheets[subreddit_name] = contents

		#self.log_info
		print('/r/%s/about/stylesheet is up to date' % (subreddit_name))


	# just for debugging
	#def run(self): self.main(r=None)


def file_get_contents(filename):
	    with open(filename) as f:
	        return f.read()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("src_path", metavar="path", type=str,
	    help="Path to file")

	args = parser.parse_args()
	filename = args.src_path

	bot = SubredditStylesheetUpdater(filename)
	bot.run()


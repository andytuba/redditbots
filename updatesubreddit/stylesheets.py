from redditbot import RedditBot
import argparse, glob, sys, itertools
import re

# Derived from https://www.reddit.com/r/reddithax/comments/2nytff/a_python_bot_to_update_your_subreddits_css_in/
class SubredditStylesheetUpdater(RedditBot):
	app_id = 'DPuHaFaQZcBO6g'
	app_uri = 'https://www.reddit.com/r/RESUpdates/'
	app_scopes = 'modconfig'

	loops = 0

	stylesheets = {
		'example': 'body { background: white; }'
	}

	def main(self, r):
		glob = self.filename_param()
		self.log_debug('File glob: %s' % glob)
		for filename in self.files(glob):
			self.log_debug('Handling %s' % filename)
			subreddit_name = re.match(r'^(\w\d_)+', filename).group(1)
			contents = file_get_contents(filename)

			self.log_debug("/r/%s will be updated with: \n%s" % (subreddit_name, contents))

			if self.stylesheets[subreddit_name] != contents:
				self.log_info('/r/%s/about/stylesheet is updating...' % (subreddit_name))
				r.set_stylesheet(subreddit_name, contents)
				self.stylesheets[subreddit_name] = contents

			self.log_info('/r/%s/about/stylesheet is up to date' % (subreddit_name))



def filename_param():
	parser = argparse.ArgumentParser()
	parser.add_argument("src_path", metavar="path", type=str,
	    help="Path to files to be merged; enclose in quotes, accepts * as wildcard for directories or filenames")

	args = parser.parse_args()
	return args.src_path

def files():
	glob_value = filename_param()
	files = glob.iglob(glob_value)

	#Should I just return files here?
	try:
	    first_file = files.next()
	except StopIteration:
	    print('File does not exist: %s' % glob_value)
	    sys.exit(1)

	return itertools.chain([first_file], files)

def file_get_contents(filename):
	    with open(filename) as f:
	        return f.read()







if __name__ == '__main__':
    bot = SubredditStylesheetUpdater()
    bot.run()


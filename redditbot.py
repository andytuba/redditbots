# Derived from https://github.com/voussoir/reddit/commit/bf3903249fe2063d174268511cb5d76b590bc723#diff-1bae6b687c5d1e9ab80ba0bfe3ebd96a
# /u/GoldenSights, /u/andytuba
import praw
#import sqlite3
import time
import traceback
import os
from .logger import VerboseLogger

class RedditBot(Object, VerboseLogger):
    loops = -1
    wait = 60

    attr_env_mapping = {
        # https://www.reddit.com/comments/3cm1p8/how_to_make_your_bot_use_oauth2/
        'useragent': 'REDDIT_APP_USERAGENT',
        'app_id': 'REDDIT_APP_ID',
        'app_secret': 'REDDIT_APP_SECRET',
        'app_uri': 'REDDIT_APP_URI',
        'app_refresh': 'REDDIT_APP_SCOPES', #https://www.reddit.com/r/GoldTesting/comments/3chbrm/all_oauth_scopes/

        'loops': 'REDDIT_APP_LOOPS', # The number of times the bot should run before quitting. -1 for infinite, 1 for once, 2 for twice, etc. Runs at least once
        'wait': 'REDDIT_APP_WAIT', # The number of seconds between each cycle. The bot is completely inactive during this time.
    }

    def main(self):
        raise NotImplementedError


    def __init__(self):
        self.set_attr_from_env()

    def set_attr_from_env(self):
        for (attr, env) in enumerate(self.attr_env_mapping):
            value = os.environ.get(env)
            if env is not None:
                setattr(self, attr, value)

    def run(self):
        #sql = sqlite3.connect('filename.db')
        #cur = sql.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS tablename(column TEXT)')

        print('Logging in.')
        r = praw.Reddit(self.useragent)
        r.set_oauth_app_info(self.app_id, self.app_secret, self.app_uri)
        r.refresh_access_information(self.app_refresh)

        while True:
            print('Running main')
            try:
                self.main(r)
            except Exception as e:
                traceback.print_exc()
            if LOOPS == 0:
                break
            LOOPS--

            time.sleep(sleep.wait)
            print('Running again in %d seconds\n' % sleep.wait)



if __name__ == '__main__':
    bot = RedditBot()
    bot.run()

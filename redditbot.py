# Derived from https://github.com/voussoir/reddit/commit/bf3903249fe2063d174268511cb5d76b590bc723#diff-1bae6b687c5d1e9ab80ba0bfe3ebd96a
# /u/GoldenSights, /u/andytuba
import praw
#import sqlite3
import time
import traceback
import os
import sys
#from .logger import VerboseLogger

class RedditBot(object): #, VerboseLogger):
    # Bot OAuth config
    # https://www.reddit.com/comments/3cm1p8/how_to_make_your_bot_use_oauth2/
    useragent = 'generic-script-by-u-andytuba'
    app_id = ''
    app_secret = ''
    app_uri = 'https://localhost/auth/'
    #https://www.reddit.com/r/GoldTesting/comments/3chbrm/all_oauth_scopes/
    app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'

    # User-specific OAuth data
    app_refresh_token = None #Refresh token

    # Bot config
    loops = -1
    wait = 60

    attr_env_mapping = {
        'app_secret': 'REDDIT_APP_SECRET',
        'app_uri': 'REDDIT_APP_URI',
        'app_refresh_token': 'REDDIT_APP_REFRESH',

        'loops': 'REDDIT_APP_LOOPS', # The number of times the bot should run before quitting. -1 for infinite, 1 for once, 2 for twice, etc. Runs at least once
        'wait': 'REDDIT_APP_WAIT', # The number of seconds between each cycle. The bot is completely inactive during this time.
    }

    def set_attr_from_env(self):
        for attr, env in self.attr_env_mapping.iteritems():
            value = os.environ.get(env)
            if value is not None:
                print('Set self.%s = environ["%s"]' % (attr, env)) #log_debug
                setattr(self, attr, value)

    def main(self):
        raise NotImplementedError

    def __str__(self):
        return '<RedditBot ua="%s", id="%s", scopes="%s">' % (self.useragent, self.app_id, self.app_scopes)

    def __init__(self):
        self.set_attr_from_env()

    def run(self):
        print('Config: %s' % self) #log_debug

        #sql = sqlite3.connect('filename.db')
        #cur = sql.cursor()
        #cur.execute('CREATE TABLE IF NOT EXISTS tablename(column TEXT)')


        print('Logging in %s (%s)' % (self.useragent, self.app_id)) #self.log_debug
        r = praw.Reddit(self.useragent)
        r.set_oauth_app_info(client_id=self.app_id, client_secret=self.app_secret, redirect_uri=self.app_uri)

        if self.app_refresh_token is None:
            authorize_url = r.get_authorize_url('...', self.app_scopes, True)
            print ('!!! Visit:   %s\nand copy that token here: ' % authorize_url)
            self.app_refresh_token = sys.stdin.readline()
            print('!!! To avoid this when invoking this script in the future, `export %s=%s' % (self.attr_env_mapping['app_refresh_token'], self.app_refresh_token))

        r.refresh_access_information(self.app_refresh)

        while True:
            print('Running main')   #self.log_debug
            try:
                self.main(r)
            except Exception as e:
                #if self.verbosity >= self.VERBOSITY.WARNING
                traceback.print_exc()
            if LOOPS == 0:
                break
            LOOPS -= 1

            time.sleep(sleep.wait)
            print('Running again in %d seconds\n' % sleep.wait) #self.log_info



if __name__ == '__main__':
    bot = RedditBot()
    bot.run()

def VerboseLogger(object):
    VERBOSITY = {
        'DEBUG': 1
        'INFO': 2
        'WARNING': 3
        'ERROR': 4
    }
    verbosity = VerboseDebugger.VERBOSITY.WARNING

    def log(self, verbosity, msg):
        if self.verbosity < verbosity:
            return

        print(msg)

    def log_debug(self, msg):
        self.log(VerboseDebugger.VERBOSITY.DEBUG, msg)

    def log_info(self, msg):
        self.log(VerboseDebugger.VERBOSITY.INFO, msg)

    def log_warning(self, msg):
        self.log(VerboseDebugger.VERBOSITY.WARNING, msg)

    def log_error(self, msg):
        self.log(VerboseDebugger.VERBOSITY.error, msg)

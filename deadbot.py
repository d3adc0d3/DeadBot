#!/usr/bin/env python

# TODO: dynamic config reloading
# TODO: add command's white/blacklists

# TODO: allow to fill white/blacklists in runtime
# TODO: allow to fill playlist in runtime

# TODO: save and load white/blacklists on run/exit
# TODO: save and load playlist on run/exit

# TODO: keep viewer list

# TODO: rename some extensions (greeter, leaver)

# TODO: python2-compatible
# TODO: allow using youtube playlist as initial playlist
# TODO: fix youtube bug
# TODO: restart crushed mpv

# TODO: let mark commands as favored-only
# TODO: let write config in CSON and/or YAML

# TODO: add "dummy" mode which will print messages instead of seding (for testing)
# TODO: catch "ws already closed" on-quit exception

# TODO: catch config/parsing exceptions and show it better way

import sys
import json

import parser

def log_exception(exception):
	print(exception)

def observe(function, *args, **kwargs):
	try: function(*args, **kwargs)
	except Exception as exception: log_exception(exception)

def get_config(args):
	if len(args) == 1: config_file = args[0]
	else: config_file = '~/.deadbot.json'

	return json.load(open(config_file))

def main(args):
	config = get_config(args)

	manager = parser.build_manager(config)
	observe(manager.wait)

if __name__ == '__main__':
	main(sys.argv[1:])

from extensions import manager

def build_manager(config):
	engine = build_engine(config)
	extension_names, extensions = build_extensions(config)
	return manager.Manager(config['manager'], engine, extensions, extension_names)

def build_engine(config):
	if config['engine']['service'] == 'livecoding.tv':
		from engines import livecoding
		return livecoding.Engine(config['engine'])

def build_extensions(config):
	return zip(*[(name, build_extension(name, config))
		for name, config in config['extensions'].items()
	])

# TODO: getting extensions dynamicaly
def build_extension(name, config):
	if name == 'spammer':
		from extensions import spammer
		return spammer.Extension(config)
	elif name == 'greeter':
		from extensions import greeter
		return greeter.Extension(config)
	elif name == 'leaver':
		from extensions import leaver
		return leaver.Extension(config)
	elif name == 'commands':
		from extensions import commands
		return commands.Extension(config)
	elif name == 'player-control':
		player = build_player(config['player'])
		scraper = build_scraper(config['scraper'])
		from extensions import player_control
		return player_control.Extension(config, player, scraper)
	elif name == 'variables':
		from extensions import variables
		return variables.Extension(config)
	elif name == 'filesystem':
		from extensions import filesystem
		return filesystem.Extension(config)
	elif name == 'uptime':
		from extensions import uptime
		return uptime.Extension(config)
	elif name == 'voting':
		from extensions import voting
		return voting.Extension(config)

def build_player(config):
	if config['name'] == 'mpv':
		from extensions.players import mpv
		return mpv.Player(config['config'])

def build_scraper(config):
	if config['name'] == 'youtube':
		from extensions.scrapers import youtube
		return youtube.Scraper()

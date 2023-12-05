from environs import Env
env = Env()
env.read_env()


def inter(*args):
	return int(args)
ADMINS = 590018906, 6558982323, 5431925010
admins = list(map(lambda x: int(x), (env('ADMINS')).split(', ')))
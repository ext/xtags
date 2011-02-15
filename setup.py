from setuptools import setup, find_packages

setup(
	name = "xtags",
	version = '0.1',
	packages = find_packages('src'),
	package_dir = {'':'src'},
	
	entry_points = """
[console_scripts]
xtags = xtags:run
""",

	author = 'David Sveningsson',
	author_email = 'ext@sidvind.com',
	url = None,
	description = 'Rudimentary implementation of my dream-filesystem, but built with symlinks and only works on directories',
)

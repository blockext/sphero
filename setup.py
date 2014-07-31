import re
from setuptools import setup


version = re.search("__version__ = '([^']+)'",
                    open('blockext_sphero/__init__.py').read()).group(1)


setup(name = 'blockext-sphero',
      version = version,
      author = 'Tim Radvan, Connor Hudson',
      author_email = 'blob8108@gmail.com',
      url = 'https://github.com/blockext/sphero',
      description = 'Orbotix Sphero extension for Scratch 2.0 and Snap!',
      license = 'MIT',
      packages = ['blockext_sphero'],
      install_requires = [
          'blockext == 0.2.0a2',
          'sphero',
      ],
      classifiers = [
        "Programming Language :: Python",
      ],
)

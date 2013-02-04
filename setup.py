# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup, find_packages

version = __import__('star').__version__

LONG_DESCRIPTION = """
"""

def long_description():
    """
    """
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-ilike',
      version=version,
      author='Andreas Neumeier',
      author_email='andreas@neumeier.org',
      description='Django liking and starring simple.',
      license='BSD',
      keywords='django, like, star, track, application',
      url='https://github.com/andreasneumeier/star',
      download_url='https://github.com/andreasneumeier/star',
      packages=['star', 'star.templatetags',],
      package_data={'star': ['locale/*/LC_MESSAGES/*']},
      long_description=long_description(),
      install_requires=['django>=1.4.1', ],
      classifiers=['Framework :: Django',
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.7'])


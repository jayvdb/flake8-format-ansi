# -*- coding: utf-8 -*-
"""ANSI error format plugin for flake8."""
from __future__ import absolute_import, unicode_literals

__version__ = '0.1.0'
__author__ = 'John Vandenberg'
__email__ = 'jayvdb@gmail.com'
__url__ = 'https://github.com/jayvdb/flake8-format-ansi'
__license__ = 'MIT License'


class ANSIFormatExtension(object):

    """Flake8 plugin for formatting errors using ANSI."""

    name = __name__.replace('_', '-')
    version = __version__

    def __init__(self):
        """Constructor."""
        # Must exist for flake8 inspection of the extension
        pass

    @classmethod
    def parse_options(cls, options):
        """Parse options and activate ansi sequences."""
        options.format = options.format.replace('\\e', '\x1b')

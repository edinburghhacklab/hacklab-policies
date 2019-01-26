# -*- coding: utf-8 -*-

import os

needs_sphinx = '1.3'
extensions = []
source_suffix = ['.rst']

project = u'Edinburgh Hacklab Policies'
copyright = u'2018-2019, Edinburgh Hacklab'
author = u'Edinburgh Hacklab'

master_doc = 'index'

language = None
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

html_theme = 'bizstyle'
html_title = project
html_logo = 'logo.png'
html_favicon = 'favicon.ico'

linkcheck_timeout = 60

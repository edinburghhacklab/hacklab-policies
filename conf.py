# -*- coding: utf-8 -*-

import os

needs_sphinx = '1.3'
extensions = ['rst2pdf.pdfbuilder']
pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Edinburgh Hacklab'),]
source_suffix = ['.rst']

project = u'Edinburgh Hacklab Policies'
copyright = u'2018-2019, Edinburgh Hacklab'
author = u'Edinburgh Hacklab'

master_doc = 'index'

language = None
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'
html_title = project
html_logo = 'logo.png'
html_favicon = 'favicon.ico'

linkcheck_timeout = 60

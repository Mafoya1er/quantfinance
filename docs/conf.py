

import os
import sys


sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'quantfinance'
copyright = '2025, Marcel ALOEKPO'
author = 'Marcel ALOEKPO'


release = '0.1.1'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser', 
]

templates_path = ['_templates']


exclude_patterns = []


html_static_path = ['_static']
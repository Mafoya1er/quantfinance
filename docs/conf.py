

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
    'sphinx.ext.napoleon',  # Pour docstrings Google/NumPy style
    'sphinx.ext.intersphinx',  # Pour liens vers d'autres docs
    'myst_parser',  # Si tu utilises Markdown
    'sphinx_copybutton',  # Pour copier le code
]

templates_path = ['_templates']


exclude_patterns = []

html_static_path = ['_static']



# Pour copier le code
copybutton_prompt_text = ">>> "
copybutton_prompt_is_regexp = True
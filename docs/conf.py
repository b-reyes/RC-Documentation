from recommonmark.parser import CommonMarkParser

project = "Research Computing\nUniversity of Colorado Boulder"

html_title = "Research Computing University of Colorado Boulder"

master_doc = 'index'

extensions = [
    'sphinx_markdown_tables', 'myst_parser', 'sphinx_copybutton'
]

source_suffix = ['.rst', '.md']

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_book_theme'

html_static_path = ['_static']

html_css_files = ["css/custom.css"]

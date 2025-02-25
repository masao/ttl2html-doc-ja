# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ttl2html'
copyright = '2023-2025, Masao Takaku'
author = 'Masao Takaku'

# release = '0.1'
# version = '0.1'

# -- General configuration

language = 'ja'

master_doc = 'index'

extensions = [
#    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

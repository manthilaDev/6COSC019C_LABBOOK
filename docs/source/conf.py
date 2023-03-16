# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lab Progress Book'
copyright = '2023, Manthila'
author = 'Manthila'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'docxsphinx']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'piccolo_theme'
html_static_path = ['_static']

# Piccolo theme specific config 
html_logo = './img/logo.png'
html_theme_options = {
    # Note how we can include links:
    "banner_text": 'Please note the content volatile and not intented as full proof solutions'
}

# myst_configurations to add Images to documents
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "html_image"
    ]
# Rinoh PDF generation config
rinoh_documents = [dict(doc='index',
                        target='log_book',
                        toctree_only= True,
                        template='custom_template.rst')]
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UR Documentation Template'
copyright = '2024, PHYE'
author = 'PHYE'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_favicon',
    'sphinx_multiversion',
    'sphinx_new_tab_link',
    'sphinx_rtd_theme',
    'sphinx_simplepdf',

]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]
html_static_path = ['_static']
html_logo = ""
html_favicon = ""
html_theme_options = {
    'analytics_id': 'G-XXX',
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'globaltoc_collapse': True,
    'globaltoc_maxdepth': None,
}
html_show_sourcelink = False
html_show_sphinx = False

locale_dirs = ['locale/'] 

simplepdf_debug = True

simplepdf_vars = {
    'primary': '#01579B',
    'primary-opaque': '1, 87, 155, 0.5',
    'secondary': '#039BE5',
    'cover': '#FFFFFF',
    'white': '#FFFFFF',
    'links': '#4FC3F7',
    'cover-bg': 'url(cobots.jpeg) no-repeat center',
    'cover-overlay': 'rgba(100, 181, 246, 0.8)',
    'top-left-content': 'counter(page)',
    'bottom-center-content': '"Custom footer content"',
}

# -- Sphinx multiversion options
# https://holzhaus.github.io/sphinx-multiversion/master

# smv_tag_whitelist = r'^.*$'                       # Include all tags

# smv_branch_whitelist = None                         # Include no branches
# smv_branch_whitelist = r'^master$'                # Include master branch

# smv_remote_whitelist = None                       # Only use local branches
# smv_remote_whitelist = r'^origin$'                  # Use branches from origin
# smv_remote_whitelist = r'^(origin|upstream)$'     # Use branches from origin and upstream
import os, sys, subprocess
from pathlib import Path

projects_path = os.path.abspath('../../')
sys.path.append(projects_path)

# fmt: off
from decore_Page.source._classes import *
from decore_Page.source._directives import *
# fmt: on

def get_language(app):
    html_context = {
        'language': app.config.language,
    }

def on_build_finished(app, exception):
    if not exception:
        if app.builder.name == 'gettext':
            t_lang = app.config.language
            cmd = ['sphinx-intl', 'update', '-p', 'source/_text', '-l', t_lang]
            subprocess.run(cmd, cwd=os.path.abspath('.'), check=True)
            app.config.localizer.translate_po_file(Path('source/_locale/'+t_lang+'/LC_MESSAGES').joinpath('docs.po'))

def setup(app):
    app.config['localizer'] = Localizer(app.config.language)
    app.add_directive('html-modal-image', Html_modal_image)
    app.add_directive('html-inpage-nav', Html_inpage_nav)
    app.add_directive('page-tabs', Page_tabs)
    app.add_directive('page-feature-pane', Page_feature_pane)
    app.connect('builder-inited', get_language)
    app.connect('build-finished', on_build_finished)
#     from decore_Page.helper import split_rst_file
#     print ('DECORE_BASE_PATH: '+ projects_path)
#     print("Hello World!")
#     split_rst_file(Path('../decore_base').joinpath('README.rst'), Path('source').joinpath('base'), ['notes'])


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'decore Base'
copyright = '2023, Jean Rohark'
author = 'Jean Rohark'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx_copybutton', 'sphinx_favicon', "sphinx_design", 'sphinx_sitemap', 'sphinx_rst_builder', 'sphinxcontrib.mermaid']

locale_dirs = ['_locale/']
gettext_compact = "docs"

language = 'de'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

add_module_names = False
autodoc_member_order = 'bysource'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'decore Base | UI fastly'

html_extra_path = ['_files']

html_directory_suffix = '/'

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
   "show_toc_level": 2,
#    "navbar_align": "right",
   "logo": {
        "text": "decore Base | UI fastly",
        },
    "footer_start": None,
    "footer_end": ["copyright"],
    "show_prev_next": False,
}

html_static_path = ['_static']

html_css_files = [
    'styles/custom.css',
]

html_show_sourcelink = False

html_logo = "_static/logo.png"

favicons = [
    {"href": "favicon.ico"},
]

html_baseurl = 'https://www.decore.dev/'
sitemap_filename = 'sitemap.xml'
sitemap_url_scheme = "{link}"

# html5_polyglot_doctype = True
# html5_extra_attrs = {
#     '*': ['data-bs-toggle', 'data-bs-target']
# }
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = "Rosetta"
copyright = "2023, Kéita A. Yokoyama"
author = "Kéita A. Yokoyama"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # convert Google/NumPy-style docstrings to RST
    "sphinxcontrib.matlab",  # process Matlab code comments with Sphinx
    "myst_parser",  # convert Markdown (MyST) to RST
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx.
language = "en-us"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Multi-programming language support --------------------------------------
# Do not set a primary domain. This forces us to explicitly specify whether
# code is rendered as Python, Matlab, or another language.
primary_domain = None

# -- HTML output -------------------------------------------------------------
html_static_path = ["_static"]
html_title = "Rosetta Documentation"
html_theme = "furo"
html_theme_options = {
    "light_logo": "rosetta-logo-dark.svg",
    "dark_logo": "rosetta-logo-light.svg",
    "sidebar_hide_name": True,
    "announcement": None,
    "source_repository": "https://github.com/rosetta-code/rosetta-doc/",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

# Render some text using Pygments
# pygments_style = ''

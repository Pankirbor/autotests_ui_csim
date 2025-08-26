import os
import sys

# Добавляем путь к папке с вашим проектом (на уровень выше от /docs)
sys.path.insert(0, os.path.abspath("../../"))

project = "Test Framework Template"
copyright = "2025, Panov Kirill"
author = "Panov Kirill"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Главное расширение для автоматического чтения docstrings
    "sphinx.ext.napoleon",  # Для поддержки Google-стиля и NumPy-стиля
    "sphinx.ext.viewcode",  # Добавляет ссылки на исходный код
    "sphinx_rtd_theme",  # Для современной темы (если установили)
]

templates_path = ["_templates"]
exclude_patterns = []

language = "ru"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

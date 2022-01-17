========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/zmbRELEV/badge/?style=flat
    :target: https://zmbRELEV.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/j3ffsilva/zmbRELEV/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/j3ffsilva/zmbRELEV/actions

.. |requires| image:: https://requires.io/github/j3ffsilva/zmbRELEV/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/j3ffsilva/zmbRELEV/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/j3ffsilva/zmbRELEV/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/j3ffsilva/zmbRELEV

.. |version| image:: https://img.shields.io/pypi/v/zmbrelev.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/zmbrelev

.. |wheel| image:: https://img.shields.io/pypi/wheel/zmbrelev.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/zmbrelev

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/zmbrelev.svg
    :alt: Supported versions
    :target: https://pypi.org/project/zmbrelev

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/zmbrelev.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/zmbrelev

.. |commits-since| image:: https://img.shields.io/github/commits-since/j3ffsilva/zmbRELEV/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/j3ffsilva/zmbRELEV/compare/v0.0.0...main



.. end-badges

This project lets you train a classifier on news about racial discrimination

* Free software: BSD 2-Clause License

Installation
============

::

    pip install zmbrelev

You can also install the in-development version with::

    pip install https://github.com/j3ffsilva/zmbRELEV/archive/main.zip


Documentation
=============


https://zmbRELEV.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

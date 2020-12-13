#!/usr/bin/env bash
#
# This file is part of GeoServer Installer CLI.
# Copyright (C) 2021 INPE.
#
# GeoServer Installer CLI is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle geoserver_installer examples tests setup.py && \
isort geoserver_installer examples tests setup.py --check-only --diff && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest && \
pytest

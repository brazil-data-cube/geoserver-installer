#
# This file is part of GeoServer Installer CLI.
# Copyright (C) 2021 INPE.
#
# GeoServer Installer CLI is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for GeoServer Installer CLI."""

import pytest

from geoserver_installer.extension import get_geoserver_extensions


@pytest.mark.parametrize(
    'geoserver_version', ['2.15.0', '2.16.0', '2.17.0', '2.18.0']
)
def test_get_geoserver_extensions_valid_geoserver_version(geoserver_version):
    assert type(get_geoserver_extensions(g_version=geoserver_version)) == list
    assert len(get_geoserver_extensions(g_version=geoserver_version)) != 0


@pytest.mark.parametrize(
    'geoserver_version', ['2.15.x', '2.16.x', '2.17.x', '2.18.x']
)
def test_get_geoserver_extensions_invalid_geoserver_version(geoserver_version):
    with pytest.raises(RuntimeError):
        get_geoserver_extensions(geoserver_version)

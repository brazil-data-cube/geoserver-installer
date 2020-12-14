"""
This file is part of Repository of Dockerfiles for the Brazil Data Cube Project. Copyright (C) 2021 INPE.

The Repository of Dockerfiles for the Brazil Data Cube Project is free software; you can redistribute it and/or modify
it under the terms of the MIT License; see LICENSE file for more details.
"""

import os

import click

from .extension import (get_geoserver_extensions,
                        get_geoserver_extensions_community, select_extensions)
from .image import create_dockerfile, create_install_script
from .utils import copy_script_files


@click.group()
def cli():
    """geoserver_installer cli."""
    pass


@cli.command(name="build", help="Create custom GeoServer Dockerfiles")
@click.option("--version", help="Specifies the used version of the geoserver", required=True, type=str)
@click.option("--disable-community-extensions",
              help="Disable selection of community plugins", type=bool, is_flag=True)
@click.option("--disable-all-extensions",
              help="Disable selection of all plugins", type=bool, is_flag=True)
def build(version, disable_community_extensions, disable_all_extensions) -> None:
    """Create custom GeoServer Dockerfiles."""
    extensions = []

    if not disable_all_extensions:
        extensions = select_extensions(get_geoserver_extensions(g_version=version))

        if not disable_community_extensions:
            community_version = version[:-1] + "x"
            community_extensions = get_geoserver_extensions_community(g_version=community_version)
            extensions.extend(select_extensions(community_extensions, min_selection_count=0))

    install_path = create_install_script(extensions, "./install.sh",
                                         "/usr/local/tomcat/webapps/geoserver/WEB-INF/lib")
    create_dockerfile(install_path, g_version=version)

    # Copy files to build dockerfile
    os.chmod(install_path, 0o755)
    copy_script_files(os.getcwd())

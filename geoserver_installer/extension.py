"""
This file is part of Repository of Dockerfiles for the Brazil Data Cube Project. Copyright (C) 2021 INPE.

The Repository of Dockerfiles for the Brazil Data Cube Project is free software; you can redistribute it and/or modify it
under the terms of the MIT License; see LICENSE file for more details.
"""

import requests
from bs4 import BeautifulSoup

SOURCE_FORCE_OFFICIAL_EXTENSIONS_URL = "https://sourceforge.net/projects/geoserver/files/GeoServer/{}/extensions/"
SOURCE_FORCE_COMMUNITY_EXTENSIONS_URL = "https://build.geoserver.org/geoserver/{}/community-latest/"


def get_geoserver_extensions(g_version: str = "2.18.0") -> list:
    """Retrieve available official extensions for the GeoServer SourceForge repository.

    This function retrieves the available official extensions on SourceForge.net GeoServer Repository.
    Args:
        g_version (str): GeoServer Version
    Returns:
        list: List with URL of all extensions found
    See:
        GeoServer Versions: https://build.geoserver.org/geoserver
    """
    extension_url = SOURCE_FORCE_OFFICIAL_EXTENSIONS_URL.format(g_version).strip()
    page = requests.get(extension_url)

    if page.status_code == 200:
        bs = BeautifulSoup(page.text, "html.parser")
        extension_ths = bs.find_all("th")

        urls = []
        # Starts at 5 since before this value all `ths` are not plugins
        for i in range(5, len(extension_ths)):
            urls.append(
                "/".join(extension_ths[i].a.get("href").split("/")[0:-1])
            )
        return urls
    else:
        raise RuntimeError("{} - The page of the specified version cannot be loaded".format(
            page.reason
        ))


def get_geoserver_extensions_community(g_version: str = "2.18.0") -> list:
    """Retrieve available community extensions for the GeoServer SourceForge repository.

    This function retrieves the available community extensions on SourceForge.net GeoServer Repository.
    Args:
        g_version (str): GeoServer Version
    Returns:
        list: List with URL of all extensions found
    See:
        GeoServer Versions: https://build.geoserver.org/geoserver
    """
    extension_url = SOURCE_FORCE_COMMUNITY_EXTENSIONS_URL.format(g_version).strip()
    page = requests.get(extension_url)

    if page.status_code == 200:
        bs = BeautifulSoup(page.text, "html.parser")
        return [extension_url + i.get('href') for i in bs.find_all('a')[1:]]
    else:
        raise RuntimeError("{} - The page of the specified version cannot be loaded".format(
            page.reason
        ))


def select_extensions(extensions: list, min_selection_count: int = 1) -> list:
    """Create a interactive terminal interface allowing users to select extensions.

    This function create a interactive terminal interface allow user to select extensions will be used on GeoServer.
    dockerfile
    Args:
        extensions (list): Listed link of all extensions to display
        min_selection_count (int): Minimum values to select on pick interface
    Returns:
        list: List with user-selected extensions
    """
    from pick import pick

    options = [i.split("/")[-1] for i in extensions]
    # **args not used to limit the possibility of menu changes
    selected = pick(options, title="Select the desired extension",
                    min_selection_count=min_selection_count, multi_select=True)

    return [extensions[i[1]] for i in selected]


if __name__ == "__main__":
    print(get_geoserver_extensions())

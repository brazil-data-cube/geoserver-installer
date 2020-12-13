#
# This file is part of Repository of Dockerfiles for the Brazil Data Cube Project.
# Copyright (C) 2021 INPE.
#
# The Repository of Dockerfiles for the Brazil Data Cube Project is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#


def create_install_script(extensions_url: list, file_path: str, lib_path: str) -> str:
    """Function for creating plugin installation script
    Args:
        extensions_url (list): URL list of extensions to install
        file_path (str): Absolute path where the installation file will be saved
        lib_path (str): Path to directory where GeoServer extensions are
    Returns:
        str: Path to plugins installation file
    """

    with open(file_path, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("""
        apt update && apt install unzip
        """.strip() + "\n")
        f.write("cd {}".format(lib_path).strip() + "\n")

        for extension_url in extensions_url:
            extension_name = extension_url.split("/")[-1]
            f.write("wget {URL} && unzip -o -q -d \"${PLUGINS_DIR}\" {FILE} && rm {FILE}\n".format(
                URL=extension_url, FILE=extension_name, PLUGINS_DIR="{PLUGINS_DIR}"
            ))

    return file_path


def create_dockerfile(file_path: str, g_version: str = "2.8.5", dockerfile_path: str = "./Dockerfile") -> None:
    """Function to generate image Dockerfile with plugins defined in installation script
    Args:
        file_path (str): Path to installation file
        g_version (str): GeoServer Version
        dockerfile_path (str): Absolute path to the Dockerfile file that will be generated
    Returns:
        None
    """

    with open(dockerfile_path, "w") as f:
        dockerfile_content = """
            FROM tomcat:8.0-jre8

            # Customizable Variables
            ENV GEOSERVER_VERSION "{GEOSERVER_VERSION_VAR}"
            ENV GEOSERVER_URL "/geoserver"
            ENV GEOSERVER_DATA_DIR /opt/geoserver/data_dir

            # Environment Variables
            RUN mkdir -p $GEOSERVER_DATA_DIR

            # Install GeoServer
            RUN wget --no-verbose "http://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/geoserver-${GEOSERVER_VERSION}-war.zip" && \
                unzip geoserver-${GEOSERVER_VERSION}-war.zip && \
                mv geoserver.war /root/ && \
                rm geoserver-${GEOSERVER_VERSION}-war.zip

            COPY {SCRIPT_FILE} /
            COPY docker-entrypoint.sh /

            ENTRYPOINT [ "/docker-entrypoint.sh" ]
            """.format(SCRIPT_FILE=file_path, GEOSERVER_VERSION="{GEOSERVER_VERSION}", GEOSERVER_VERSION_VAR=g_version)
        f.write("\n".join([i.strip() for i in dockerfile_content.split("\n")]))

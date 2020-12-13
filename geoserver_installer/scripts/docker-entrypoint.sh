#!/bin/bash
#
# This file is part of the Repository of Dockerfiles for the Brazil Data Cube Project.
# Copyright (C) 2021 INPE.
#
# The Repository of Dockerfiles for the Brazil Data Cube Project is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

# Replace GeoServer path in Tomcat's configuration file (server.xml)
sed "125c<Context path=\"$GEOSERVER_URL\" docBase=\"/root/geoserver.war\"/>" /usr/local/tomcat/conf/server.xml > /root/server.xml
mv /root/server.xml /usr/local/tomcat/conf/server.xml

# If GeoServer wasn't unpacked yet, unpack it into Tomcat's GeoServer folder
export FOLDER_NAME="${GEOSERVER_URL//\//\#}"
export GEO_ROOT_DIR="${PWD}/webapps/${FOLDER_NAME:1:100}"
export PLUGINS_DIR="${GEO_ROOT_DIR}/WEB-INF/lib/"

if [ ! -d "${PLUGINS_DIR}" ]; then
  unzip -d ${GEO_ROOT_DIR} /root/geoserver.war
  /install.sh
fi

# This is the command that will run within the container.
catalina.sh run
#!/bin/bash
#
# This file is part of the Repository of Dockerfiles for the Brazil Data Cube Project.
# Copyright (C) 2021 INPE.
#
# The Repository of Dockerfiles for the Brazil Data Cube Project is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

export CATALINA_OPTS="$CATALINA_OPTS -server"
export CATALINA_OPTS="$CATALINA_OPTS -Xms2048m"
export CATALINA_OPTS="$CATALINA_OPTS -Xmx4096m"
export CATALINA_OPTS="$CATALINA_OPTS -XX:+UseParallelGC"
export CATALINA_OPTS="$CATALINA_OPTS -Duser.timezone=GMT"
export JAVA_OPTS="$JAVA_OPTS -Xms2048m -Xmx4096m -XX:+UseParallelGC"
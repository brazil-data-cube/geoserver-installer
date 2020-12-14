..
    This file is part of GeoServer-Installer
    Copyright (C) 2019-2021 INPE.

    GeoServer Installer is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Running the geoserver-installer
================================

From a terminal, after the installation, run the ``geoserver-installer`` command line tool as follow::

    $ geoserver-installer build --version 2.16.2


The above command will generate a ``Dockerfile`` for the creation of an image with the appropriated GeoServer version and an ``install.sh`` script for the installation of the selected plugins during the container startup.

If you want to know more about the command line options, try::

    $ geoserver-installer --help

    Usage: geoserver-installer [OPTIONS] COMMAND [ARGS]...

      geoserver-installer cli

    Options:
      --help  Show this message and exit.

    Commands:
      build  Create custom GeoServer Dockerfiles

The ``build`` command allows you to specify the following flags (see ``geoserver-installer build --help``):
- `--disable-community-extensions``: Disable selection of community plugins.

- ``--disable-all-extensions``: Disable selection of all plugins.


Building the GeoServer Docker Image
------------------------------------

The ``docker build`` command can be used to create the image::

    docker build --no-cache -t "bdc/geoserver:2.16.2" .

The above command will create a Docker image named bdc/geoserver and tag 2.16.2, as one can see with the ``docker images`` command::

    $ docker images

    REPOSITORY         TAG         IMAGE ID          CREATED                SIZE
    bdc/geoserver      2.16.2      429408ea2616      About a minute ago     573MB
    tomcat             8.0-jre8    8391ef8f6ae4      18 months ago          463MB

With the image generated through the build, the GeoServer container is ready for launch.

Launching a GeoServer Container
--------------------------------

The example provided in this section shows how to launch a GeoServer container with a shared volume between the host and the container. We are going to provide a volume for the GeoServer's data directory.


Let's first create a volume named ``geoserver_data`` with the ``docker volume create`` command::

    $ docker volume create geoserver_data

Next we are going to create and launch the GeoServer container::

    docker run --detach \
               --restart=unless-stopped \
               --publish 127.0.0.1:8080:8080 \
               --volume geoserver_data:/opt/geoserver/data_dir \
               --volume ${PWD}/geoserver.env.sh:/usr/local/tomcat/bin/setenv.sh \
               --env GEOSERVER_URL='/bdc/geoserver' \
               --name global_geoserver \
               bdc/geoserver:2.16.2

Let's take a look at each parameter in the above command:

- ``--detach``: tells Docker that the container will run in background (daemon).

- ``--restart=always``: tells Docker to always restart the container. This will assure that after the machine reboots the conatiner will be put to run again.

- ``--publish 127.0.0.1:8080:8080``: by default the GeoServer will be running on port 8080 of the container. You can bind a host port, such as 8080 to the container port 8080.

- ``--volume geoserver_data:/opt/geoserver/data_dir``: mount the named volume ``geoserver_data`` within the container filesystem under the ``/opt/geoserver/data_dir`` folder.

- ``--volume ${PWD}/geoserver.env.sh:/usr/local/tomcat/bin/setenv.sh``: you can inform some configurations to the Tomcat service through the ``geoserver.env.sh`` file. This file contains some examples on how to configure the amount of memory used by Tomcat and the TimeZone to be used.

- ``--env GEOSERVER_URL='/bdc/geoserver'``: this will set an evironment variable in the container that controls the suffix added to the base Tomcat URL. In the example, the GeoServer admin user interface will be available through the URL: http://localhost:8080/bdc/geoserver.

- ``--name global_geoserver``: names the container as ``global_geoserver``.

- ``bdc/geoserver:2.16.2``: specifies the Docker image to be used for the creation of the container.

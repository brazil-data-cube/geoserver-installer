..
    This file is part of GeoServer-Installer
    Copyright (C) 2019-2021 INPE.

    GeoServer Installer is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

The ``geoserver-installer`` depends essentially on `Requests <https://requests.readthedocs.io/en/master/>`_, `Pick <https://github.com/wong2/pick>`_, `Beautiful Soup <https://www.crummy.com/software/BeautifulSoup/>`_ and `Click <https://click.palletsprojects.com/en/7.x/>`_. Please, read the instructions below in order to be able to install  ``geoserver-installer``.

Production installation
-----------------------

Install from `Github <https://github.com/brazil-data-cube/geoserver-installer>`_:

    .. code-block:: shell

        $ pip3 install git+https://github.com/brazil-data-cube/geoserver-installer


Development installation
------------------------

Clone the software repository:

.. code-block:: shell

        $ git clone https://github.com/brazil-data-cube/geoserver-installer.git


Go to the source code folder:

.. code-block:: shell

        $ cd geoserver-installer


Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]


Run the tests:

.. code-block:: shell

        $ ./run-tests.sh

"""
This file is part of Repository of Dockerfiles for the Brazil Data Cube Project. Copyright (C) 2021 INPE.

The Repository of Dockerfiles for the Brazil Data Cube Project is free software; you can redistribute it and/or modify it
under the terms of the MIT License; see LICENSE file for more details.
"""

import os
import shutil


def copy_script_files(dest_path: str) -> None:
    """Copy script files on "scripts" package directory to actual working directory.

    This function copy files presented on "scripts" files located on package directory to actual working directory.
    Args:
        dest_path (str): Directory where data will be copied
    Returns:
        None
    """
    base_path = os.path.join(os.path.split(__file__)[0], "scripts")
    script_files = os.listdir(base_path)

    for script_file in script_files:
        shutil.copy(os.path.join(base_path, script_file), dest_path)

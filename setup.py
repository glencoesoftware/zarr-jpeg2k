# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENSE.txt
# file you can find at the root of the distribution bundle.  If the file is
# missing please request a copy by contacting info@glencoesoftware.com

from setuptools import setup
import os

import version


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='zarr-jpeg2k',
    version=version.getVersion(),
    description='JPEG-2000 Compression for zarr chunks',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Glencoe Software, Inc.',
    author_email='info@glencoesoftware.com',
    maintainer=None,
    maintainer_email=None,
    url='https://github.com/glencoesoftware/zarr-jpeg2k',
    install_requires=[
        'imagecodecs==2021.8.26',
        'numcodecs==0.9.1',
        'numpy>=1.15'
    ],
    python_requires='>=3.7'
    )

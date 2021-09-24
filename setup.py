# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os


def read(fname):
    """
    Utility function to read the README file.
    :rtype : String
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name = 'zarr-jpeg2k',
      version = '0.1.0',
      description = 'JPEG-2000 Compression for zarr chunks',
      long_description = read('README.md'),
      author = 'Glencoe Software, Inc.',
      author_email = 'info@glencoesoftware.com',
      maintainer = None,
      maintainer_email = None,
      url = 'https://github.com/glencoesoftware/zarr-jpeg2k',
      package_dir = {'': 'src'},
      packages = find_packages(),
      package_data = {'': ['*']},
      install_requires = [
          'imagecodecs==2020.1.31',
          'numcodecs==0.9.1',
          'numpy>=1.15'
      ],
      python_requires = '>=3.6'
    )

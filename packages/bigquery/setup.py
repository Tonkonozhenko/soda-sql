#!/usr/bin/env python
import sys
from setuptools import setup, find_namespace_packages

if sys.version_info < (3, 7):
    print('Error: Soda SQL requires at least Python 3.7')
    print('Error: Please upgrade your Python version to 3.7 or later')
    sys.exit(1)

package_name = "soda-sql-bigquery"
package_version = '2.1.0b10'
# TODO Add proper description
description = "Soda SQL BigQuery"

requires = [
    f'soda-sql-core=={package_version}',
    'google-cloud-bigquery>=2.5.0'
]
# TODO Fix the params
# TODO Add a warning that installing core doesn't give any warehouse functionality
setup(
    name=package_name,
    version=package_version,
    install_requires=requires,
    packages=find_namespace_packages(include=["sodasql*"])
)

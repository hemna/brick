import brick

from setuptools import setup, find_packages
import sys, os

setup(name='brick',
      version=brick.version,
      description="Local volume discovery and management.",
      long_description="""\
Add description""",
      author='Walter A. Boring IV',
      author_email='waboring@hemna.com',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Filesystems',
          'Topic :: System :: Operating System Kernels :: Linux',
      ],
      keywords=['kernel', 'lvm', 'volumes', 'iscsi', 'fibrechannel'],
      url='http://packages.python.org/brick',
      license='Apache License, Version 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

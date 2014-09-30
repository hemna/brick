Brick Library
===================
This library is intended to be used with the OpenStack Cinder and Nova
projects to help:
 * discover and remove remotely attached volumes
 * create local volumes from LVM 

Requirements
============

Capabilities
============


Installation
============

::

 $ python setup.py install


Unit Tests
==========

::

 $ pip install nose
 $ pip install nose-testconfig
 $ cd test
 $ nosetests


Folders
=======
* docs -- contains the documentation.
* brick -- the library
* brick/tests -- unit tests
* samples -- some sample uses


Documentation
=============

To view the built documentation point your browser to

::

  brick/docs/_build/html/index.html




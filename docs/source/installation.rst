Installing / Upgrading
======================
.. highlight:: bash


**Brick** is in the `Python Package Index
<http://pypi.python.org/pypi/cinder-brick/>`_.

Installing with pip
-------------------

We prefer `pip <http://pypi.python.org/pypi/pip>`_
to install pymongo on platforms other than Windows::

  $ pip install cinder-brick

To upgrade using pip::

  $ pip install --upgrade cinder-brick

Installing with easy_install
----------------------------

If you must install cinder-brick using
`setuptools <http://pypi.python.org/pypi/setuptools>`_ do::

  $ easy_install cinder-brick

To upgrade do::

  $ easy_install -U cinder-brick


Installing from source
----------------------

If you'd rather install directly from the source (i.e. to stay on the
bleeding edge), then check out the latest source from github and 
install the driver from the resulting tree::

  $ git clone https://github.com/hemna/cinder-brickgit
  $ cd cinder-brick
  $ python setup.py install


#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Utilities and helper functions."""


import contextlib
import os
import shutil
import tempfile

from oslo.config import cfg

from brick.initiator import connector
from brick.openstack.common import lockutils
from brick.openstack.common import log as logging
from brick.openstack.common import processutils


CONF = cfg.CONF
LOG = logging.getLogger(__name__)
ISO_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
PERFECT_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

synchronized = lockutils.synchronized_with_prefix('brick-')


def execute(*cmd, **kwargs):
    """Convenience wrapper around oslo's execute() method."""
    if 'run_as_root' in kwargs and 'root_helper' not in kwargs:
        kwargs['root_helper'] = get_root_helper()
    return processutils.execute(*cmd, **kwargs)


@contextlib.contextmanager
def temporary_chown(path, owner_uid=None):
    """Temporarily chown a path.

    :params owner_uid: UID of temporary owner (defaults to current user)
    """
    if owner_uid is None:
        owner_uid = os.getuid()

    orig_uid = os.stat(path).st_uid

    if orig_uid != owner_uid:
        execute('chown', owner_uid, path, run_as_root=True)
    try:
        yield
    finally:
        if orig_uid != owner_uid:
            execute('chown', orig_uid, path, run_as_root=True)


@contextlib.contextmanager
def tempdir(**kwargs):
    tmpdir = tempfile.mkdtemp(**kwargs)
    try:
        yield tmpdir
    finally:
        try:
            shutil.rmtree(tmpdir)
        except OSError as e:
            LOG.debug('Could not remove tmpdir: %s', e)


def get_root_helper():
    return 'sudo brick-rootwrap %s' % CONF.rootwrap_config


def brick_get_connector_properties():
    """wrapper for the brick calls to automatically set
    the root_helper needed for brick.
    """

    root_helper = get_root_helper()
    return connector.get_connector_properties(root_helper,
                                              CONF.my_ip)


def brick_get_connector(protocol, driver=None,
                        execute=processutils.execute,
                        use_multipath=False,
                        device_scan_attempts=3,
                        *args, **kwargs):
    """Wrapper to get a brick connector object.
    This automatically populates the required protocol as well
    as the root_helper needed to execute commands.
    """

    root_helper = get_root_helper()
    return connector.InitiatorConnector.factory(protocol, root_helper,
                                                driver=driver,
                                                execute=execute,
                                                use_multipath=use_multipath,
                                                device_scan_attempts=
                                                device_scan_attempts,
                                                *args, **kwargs)

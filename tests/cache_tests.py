# -*- coding: utf-8  -*-
"""API Request cache tests."""
#
# (C) Pywikibot team, 2012-2014
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id$'
#

from pywikibot.site import BaseSite
import scripts.maintenance.cache as cache

from tests import _cache_dir
from tests.aspects import unittest, TestCase


class RequestCacheTests(TestCase):

    """Validate cache entries."""

    net = False

    def _check_cache_entry(self, entry):
        self.assertIsInstance(entry.site, BaseSite)
        self.assertIsInstance(entry.site._loginstatus, int)
        self.assertIsInstance(entry.site._username, list)
        print(entry.site._loginstatus, entry.site._username)
        self.assertTrue(bool(entry.site._loginstatus < 1) !=
                        bool(entry.site._username[0]))
        self.assertIsInstance(entry._params, dict)
        self.assertIsNotNone(entry._params)
        # TODO: more tests on entry._params, and possibly fixes needed
        # to make it closely replicate the original object.

    def test_cache(self):
        cache.process_entries(_cache_dir, self._check_cache_entry)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback
import json
from os.path import isdir, realpath, join

# metadata version
version = 1

class MetadataError(Exception):
    def __init__(self, path, message):
        self.path = path
        self.message = message
        self.exc = sys.exc_info()

    def __str__(self):
        return 'xtags: %s: %s' % (self.path, self.message)

class Metadata:
    def __init__(self, folder, mode='r'):
        if not isdir(folder):
            raise MetadataError(folder, 'No such directory.')

        self._folder = realpath(folder)
        self._metadata = {
            'xtags:version': version
        }
        
        try:
            with open(join(folder, '.tag-metadata')) as fp:
                self._metadata = json.load(fp)
        except IOError: # no metadata
            # read-only, but no metadata available
            if mode == 'r':
                raise MetadataError(folder, 'No metadata.')
            # if it is write-enabled, it is ok because
            # it will be created.
        except ValueError: # corrupt metadata
            raise ValueError, 'Corrupt metadata'

    def commit(self):
        # always save using the latest version
        self._metadata['xtags:version'] = version

        with open(join(self._folder, '.tag-metadata'), 'w') as fp:
            json.dump(self._metadata, fp, indent=4)
            fp.write("\n")

    def version(self):
        return self['xtags:version']

    def __setitem__(self, k, v):
        if k[:5] == 'xtags:':
            raise ValueError, 'xtags: is a reserved prefix'

        try:
            p = v.split(',')
            if len(p) > 1:
                v = p
        except:
            pass

        self._metadata[k] = v

    def __getitem__(self, k):
        return self._metadata.get(k, None)

    def __contains__(self, k):
        return k in self._metadata

    def __str__(self):
        def to_str(x):
            if isinstance(x, list):
                return ', '.join(x)
            if isinstance(x, dict):
                return to_str(['%s: %s' % y for y in x.items()])
            return str(x)

        tags = u"\n".join([u"%-15s%s" % (k, to_str(v)) for k,v in self._metadata.items() if k[:5] != 'xtags'])
        return '''Tag metadata (v{version}) for {folder}:

{tags}'''.format(folder=self._folder, version=self.version(), tags=tags.encode('utf-8'))

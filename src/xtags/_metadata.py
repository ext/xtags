#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, traceback
import json
from os.path import isdir, realpath, join

class Metadata:
    def __init__(self, folder):
        if not isdir(folder):
            raise ValueError, 'must be directory'

        self._folder = realpath(folder)
        self._metadata = {}
        
        try:
            with open(join(folder, '.tag-metadata')) as fp:
                self._metadata = json.load(fp)
        except IOError: # no metadata
            pass
        except ValueError: # corrupt metadata
            print >> sys.stderr, "Warning, metadata is corrupt."
            traceback.print_exc(file=sys.stderr)

    def commit(self):
        with open(join(self._folder, '.tag-metadata'), 'w') as fp:
            json.dump(self._metadata, fp, indent=4)
            fp.write("\n")

    def __setitem__(self, k, v):
        try:
            p = v.split(',')
            if len(p) > 1:
                v = p
        except:
            pass

        self._metadata[k] = v

    def __getitem__(self, k):
        return self._metadata.get(k, None)

    def __str__(self):
        def to_str(x):
            if isinstance(x, list):
                return ', '.join(x)
            if isinstance(x, dict):
                return to_str(['%s: %s' % y for y in x.items()])
            return str(x)

        tags = u"\n".join([u"%-15s%s" % (k, to_str(v)) for k,v in self._metadata.items()])
        return '''Tag metadata for {folder}:

{tags}'''.format(folder=self._folder, tags=tags.encode('utf-8'))

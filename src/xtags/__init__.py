#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import inspect
import _config

action_lut = {}

def action(func):
    action_lut[func.__name__] = func
    return func

action_lut['config'] = _config.editor

@action
def view(*targets):
    pass

@action
def set(key, value, target='.'):
    """
    Add/set metadata.
    """
    pass

@action
def help(func=None):
    def getargs(x):
        args, varargs, _keywords, defaults = inspect.getargspec(x)
        if not defaults:
            defaults = []
        # create a list of (arg, default)-tuples
        args = list(zip(args, [None]*(len(args)-len(defaults)))) + list(zip(args[-len(defaults):], defaults))        
        return args, varargs

    def arg_to_str(name, default):
        if not default:
            return name.upper()
        return '[%s=%s]' % (name.upper(), default)
    
    if func is not None:
        fn = action_lut.get(func, None)
        
        if fn:
            args, varargs = getargs(fn)
            print 'Help for', func
            print func, ' '.join([arg_to_str(x,y) for x,y in args]),
            print fn.__doc__
            return
    
    print 'Usage: xtags COMMAND [ARGS]'
    print
    print 'Commands'
    for name, func in action_lut.items():
        args, varargs = getargs(func)

        print ' ', name, ' '.join([arg_to_str(x,y) for x,y in args]),
        
        if varargs:
            print '[%s...]' % varargs.upper(),
        
        print

def run():
    cmd = 'view'
    args = []
    
    try:
        x = sys.argv[1]

        # special case when the only argument is a file entry
        if not os.path.exists(x):
            cmd =  x
            args = sys.argv[2:]
        else:
            args = sys.argv[1:]
    except IndexError:
        pass
    
    func = action_lut.get(cmd, help)
    func(*args)

if __name__ == '__main__':
    run()

# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG),
# acting on behalf of its Max Planck Institute for Intelligent Systems and the
# Max Planck Institute for Biological Cybernetics. All rights reserved.
#
# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is holder of all proprietary rights
# on this computer program. You can only use this computer program if you have closed a license agreement
# with MPG or you get the right to use the computer program from someone who is authorized to grant you that right.
# Any use of the computer program without a valid license is prohibited and liable to prosecution.
# Contact: ps-license@tuebingen.mpg.de
#
#
# If you use this code in a research publication please consider citing the following:
#
# Expressive Body Capture: 3D Hands, Face, and Body from a Single Image <https://arxiv.org/abs/1904.05866>
#
#
# Code Developed by:
# Nima Ghorbani <https://nghorbani.github.io/>
#
# 2018.12.13

import configparser

import itertools
from ast import literal_eval

class Configer(dict):
    def __init__(self, default_ps_fname=None, **kwargs):
        super(Configer, self).__init__(**kwargs)
        if default_ps_fname:
            parser = configparser.ConfigParser()
            parser.optionxform = str

            parser.read(default_ps_fname)
            self.default_ps = dict(list(itertools.chain(*[parser.items(section) for section in parser.sections()])))
            for k,v in self.default_ps.items():_ = self.__getattr__(k)
        else:
            self.default_ps = None

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            if self.default_ps:
                if name in self.default_ps.keys():
                    try:
                        return_val = literal_eval(self.default_ps[name])
                    except (ValueError, SyntaxError) as e:
                        #sys.stderr.write('Unable to evaluatie value for %s in Configer.\n' % name)
                        return_val = self.default_ps[name]
                    self[name] = return_val
                    return return_val
            raise(AttributeError('Key %s not exising.'%name))

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            _ = self.pop(name)
        else:
            raise AttributeError("No such attribute: " + name)

    def __repr__(self):
        return str(self.get_as_dict())

    def __str__(self):
        return str(self.get_as_dict())

    def get_as_dict(self):
        res = {}
        keys = sorted(self.keys())
        for k in keys:
            if k == 'default_ps': continue
            else: res[k] = self[k]
        return res

    def dump_settings(self, fname):
        '''
        dump current configuration to an ini file
        :param fname:
        :return:
        '''
        with open(fname,'w') as f:
            f.write('[All]\n')
            for k,v in self.get_as_dict().items():
                if isinstance(v, str):v = v.replace('\n', ' ')
                f.write('%s : %s\n'%(k,v))
        return True

    def __add__(self, other, overload=False):
        '''
        Add two configer classes to get a new one. This can be usefull if one needs to keep seperate default configurations
        :param other: the other configer class
        :param overload: if True existing keys will be overloaded. if False only new keys will be replaced.
        :return:
        '''
        current = self.get_as_dict()
        for k, v in other.get_as_dict().items():
            if overload:
                current[k] = other[k]
            else:
                if k not in current.keys():
                    current[k]= other[k]
        return Configer(**current)

    def overload(self, other):
        '''
        Adds two configer classes while overloading existing settings
        :param other: the other configer class
        :param overload: if True existing keys will be overloaded. if False only new keys will be replaced.
        :return:
        '''

        return self.__add__(other, overload=True)
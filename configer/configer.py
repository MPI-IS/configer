# Copyright 2018 Nima Ghorbani <www.linkedin.com/in/nimagbani>
#
# Licensed under the The GNU General Public License v3.0;
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        return str(self._get_as_dict())

    def __str__(self):
        return str(self._get_as_dict())

    def _get_as_dict(self):
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
            for k,v in self._get_as_dict().items():
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
        current = self._get_as_dict()
        for k, v in other._get_as_dict().items():
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
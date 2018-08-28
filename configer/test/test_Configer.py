# Copyright 2018 Nima Ghorbani
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

import unittest

class TestConfiger(unittest.TestCase):
     def test_configer(self):
         from configer import Configer
         default_ps_fname = 'sample_settings.ini'


         ps1 = Configer(default_ps_fname=default_ps_fname)
         self.assertEqual(ps1.status, None)

         ps2 = Configer(default_ps_fname=default_ps_fname, status=False)
         self.assertEqual(ps2.status, False)
         ps2.status = True
         self.assertEqual(ps2.status, True)
         ps2.new_status = True
         self.assertEqual(ps2.new_status, True)

         ps3 = Configer(default_ps_fname=default_ps_fname, **{'status': True})
         self.assertEqual(ps3.status, True)

         ps4 = Configer(default_ps_fname=default_ps_fname, status=False,**{'somethings': [1.0, 2.0]})
         self.assertEqual(ps4.status, False)

         ps5 = ps4 + ps3
         self.assertEqual(ps5.status,False)
         self.assertEqual(ps5.somethings, [1.0, 2.0])

         ps6 = ps4.overload(ps3)
         self.assertEqual(ps6.status,False)

if __name__ == '__main__':
    unittest.main()

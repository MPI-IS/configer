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

import pkg_resources
import unittest

class TestConfiger(unittest.TestCase):
     def test_configer(self):
         from configer import Configer

         default_ps_fname = pkg_resources.resource_filename('tests', 'sample_settings.ini')

         ps1 = Configer(default_ps_fname=default_ps_fname)
         self.assertIsNone(ps1.status)

         ps2 = Configer(default_ps_fname=default_ps_fname, status=False)
         self.assertFalse(ps2.status)
         ps2.status = True
         self.assertTrue(ps2.status)
         ps2.new_status = True
         self.assertTrue(ps2.new_status)

         ps3 = Configer(default_ps_fname=default_ps_fname, **{'status': True})
         self.assertTrue(ps3.status)

         ps4 = Configer(default_ps_fname=default_ps_fname, status=False,**{'somethings': [1.0, 2.0]})
         self.assertFalse(ps4.status)

         ps5 = ps4 + ps3
         self.assertFalse(ps5.status)
         self.assertEqual(ps5.somethings, [1.0, 2.0])

         ps6 = ps4.overload(ps3)
         self.assertTrue(ps6.status)

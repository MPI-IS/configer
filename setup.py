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

from distutils.core import setup

setup(name='configer',
      version='0.9',
      packages=['configer'],
      package_data={'configer': ['test/*.py','test/*.ini', '../README.md']},
      author='Nima Ghorbani',
      author_email='nima.gbani@gmail.com',
      maintainer='Nima Ghorbani',
      maintainer_email='nima.gbani@gmail.com',
      url='https://github.com/nimagbani/configer',
      description='Easy configuration of arguments in a python code!',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      license=u"GNU Affero General Public License, version 3",
      classifiers=[
          "Intended Audience :: Developers",
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          "Natural Language :: English",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: POSIX",
          "Operating System :: POSIX :: BSD",
          "Operating System :: POSIX :: Linux",
          "Operating System :: Microsoft :: Windows",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6"],
      )
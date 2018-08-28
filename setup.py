from distutils.core import setup

setup(name='Configer',
      version='0.8',
      packages=['Configer'],
      package_data={'Configer': ['test/*.py','test/*.ini']},
      author='Max Planck Perceiving Systems - Body Group',
      author_email='nima.gbani@gmail.com',
      maintainer='Nima Ghorbani',
      maintainer_email='nima.gbani@gmail.com',
      url='https://www.linkedin.com/in/nimagbani/',
      description='Easy configuration for managing arguments in a python code!',
      long_description="""This package makes python's famous ConfigParser even simpler. 
            You get a flattened ConfigParser with extra functionality: 
            access setting values with dot-access, dump settings to a file, 
            and add different settings while choosing to overload previous one. """,
      license='gpl-3.0')

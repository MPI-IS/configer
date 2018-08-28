**Configer** helps with easy configuration of arguments in a python code. When Python programs grow large, one would eventually need a way to load configurations through a file. The common answer to this would by Python's ConfigParser. But at least I find the resul of using ConfigParse an ugly code:
```
import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("c:\\tomorrow.ini")
Config.get(section, option)
```
That's why I packageg my solution to this issue. Configer basically gives you a  flattened ConfigParser with extra functionality:
- dot-access of values in the settings file
- dump settings to a file for later use
- add different settings while choosing to overload previous one.
Overall Configer will be a sleek way to disentangle settings away from the mechanics. An exact copy of the above code will be:
```
from Configer import Configer
Config = Configer(default_ps_fname='c:\\tomorrow.ini')
Config.option
```
Note that you don't have sections anymore and access option with a dot-access approach. Other use cases would be:
### Loading default settings
```
default_ps_fname = 'pyconfiger/Configer/test/sample_settings.ini'
ps = Configer(default_ps_fname=default_ps_fname)
print(ps.status) # None
```
### Loading default settings while adding new arguments
```
ps = Configer(default_ps_fname=default_ps_fname, status=False)
print(ps.status) # False
ps.status = True
print(ps.status) # True
ps.new_status = True
print(ps.new_status) # True
```
### Loading default settings while initializing with a dictionary of arguments
```
ps = Configer(default_ps_fname=default_ps_fname, status=False,**{'somethings': [1.0, 2.0]})
print(ps.somethings) # [1.0, 2.0]
```
### Adding and overloading with a second Configer instance
```
ps1 = Configer(status=False)
ps2 = Configer(status=True, othersetting = 'this')

ps3 = ps1 + ps2
print(ps3.status) # False
print(ps3.othersetting) # 'this'

ps4 = ps1.overload(ps2)
print(ps4.status) # True
```

from scipy import constants
# print(dir(constants))
for it in dir(constants):
    if True and not it.startswith('__') and not 'physical_constants' and not it.startswith('_') and not 'constants' and not 'codata':
        print(it,'=',getattr(constants,it))

'''import scipy.constants as constants

for name in dir(constants):
    if name.isupper() and not name.startswith('__'):
        value = getattr(constants, name)
        print(f"{name} = {value}")'''
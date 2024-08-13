from scipy import constants
# print(dir(constants))
for it in dir(constants):
    if True and not it.startswith('__'):
        print(it,'=',getattr(constants,it))

'''import scipy.constants as constants

for name in dir(constants):
    if name.isupper() and not name.startswith('__'):
        value = getattr(constants, name)
        print(f"{name} = {value}")'''
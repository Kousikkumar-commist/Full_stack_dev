def printnos(*nos):
    for i in nos:
        print(i)
print('Printting two values')
printnos(1,2)
print('Printing three values')
printnos(10,20,30)

def print_key_values(**kwargs):
    for key in kwargs.items():
        print(key)
        #print(f"{key} = {value}")

print_key_values(name="John", age=30, country="USA")
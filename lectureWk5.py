ages_dict = {"Bill":21, "Jane":34, "Jack":56}
name = input("Name: ")
age = input("Age: ")
ages_dict[name] = age
#print(ages_dict)
for name, ages in ages_dict.items():
    print("{:10} - {:>10}".format(name, ages, end='\n'))
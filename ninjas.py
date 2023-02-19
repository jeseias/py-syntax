ninja_belts = {}
enter_another_name = False
enter_second_name = False
yes_reponses = ['y', 'yes']
num_of_belts = {}

def ninja_intro(ninjas: dict):
  for name, belt in ninjas.items():
    if belt in list(num_of_belts.keys()):
      num_of_belts[belt].append(name)
    else:
      num_of_belts[belt] = [name]

def number_of_belts(belts: list):
  for belt in set(belts):
    num = belts.count(belt)
    if num > 1:
      print(f'They are {num} {belt} belts')
    else:
      print(f'They is {num} {belt} belt')

def print_another_name(): 
  print('')
  print('--------------------------------------------------')
  print(f'{name} has been already added to the ninjas list.')
  print('')

def get_ninja_name():
  if (enter_second_name): return input('Enter a new name: ')
  if (enter_another_name): return input('Enter another name: ')
  return input('Enter your ninja name: ')

def ninjas_with_their_belts(ninjas: dict):
  for belt in list(ninjas.keys()):
    ninja_class = ninjas[belt]
    is_more_than_one = len(ninja_class) > 1
    ninja_names = ', '.join(ninja_class[0:-1]) + f' and {ninja_class[-1]}' if is_more_than_one else ', '.join(ninja_class)
    print(f'{ninja_names} are {belt} belts') if is_more_than_one else print(f'{ninja_names} is a {belt} belt')


while True:
  name = get_ninja_name()

  if name in list(ninja_belts.keys()):
    print_another_name()
    enter_another_name = True
    continue
  else:
    enter_another_name = False
    enter_second_name = True

  belt = input(f'What belt is {name}: ')
  ninja_belts[name] = belt

  response = input('Do you want to continue (y/n? ')

  if response.lower() in yes_reponses:
    print('')
    continue 
  else:
    break

ninja_intro(ninja_belts)
print('')
print('----------------------------------')
print('')
number_of_belts(list(ninja_belts.values()))

print('-----------------------')
ninjas_with_their_belts(num_of_belts)
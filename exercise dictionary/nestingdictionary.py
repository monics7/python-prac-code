# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# print('---')
# print('Total number of aliens created is '+str(len(aliens)))

# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[:5]:
#     print(alien)

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushroom', 'extra cheese']
# }

# print('You ordered a '+pizza['crust'] +
#       "-crust pizza"+" with the following toppings:")
# for topping in pizza['toppings']:
#     print('\t'+topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     print('\n' + name.title()+"'s favorite languages are:")
#     for language in languages:
#         print('\t'+language.title())


users = {
    'monics7': {
        'first': 'monica',
        'last': 'maibram',
        'location': 'moirang',
    },
    'john56': {
        'first': 'john',
        'last': 'khaidem',
        'location': 'delhi',
    },
}

for user_name, user_info in users.items():
    print('\nUsername:'+user_name)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']

    print('\tFullname:'+full_name)
    print('\tLocation:'+location)

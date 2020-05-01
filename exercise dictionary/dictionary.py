# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_languages.items():
#     print(name.title()+"'s favorite language is " + language.title())
# # print("Sarah's favorite language is "+favorite_languages['sarah'].title())
# for name in favorite_languages:
#     print(name.title())
# friends = ['phil', 'edward']
# for name in favorite_languages:
#     print(name.title())
#     if name in friends:
#         print("Hi "+name.title() +
#               " I see your favorite language is "+favorite_languages[name].title()+"!")
# if 'erin' not in favorite_languages.keys():
#     print('Erin,please take poll')

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print('key:' + key)
#     print('Value:' + value)

# rivers = {
#     'nile': 'egypt',
#     'ganga': 'india',
#     'amazon': 'usa'
# }

# for river, country in rivers.items():
#     print("The "+river.title()+" runs through "+country.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['monica', 'phil', 'robina', 'edward']

for friend in friends:
    if friend in favorite_languages.keys():
        print(friend.title() + ',your favorite language is ' +
              favorite_languages[friend].title())
    else:
        print(friend.title()+',please take a poll')

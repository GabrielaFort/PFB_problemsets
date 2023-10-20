#!/usr/bin/env python3
import sys

my_favorite_things = {'band':'RKS','plant':'iris'}
print(type(my_favorite_things))
print(my_favorite_things)

fav_band=my_favorite_things['band']

print(f'My favorite band is: {fav_band}')


fav_thing='band'

print(my_favorite_things[fav_thing])

fav_plant=my_favorite_things['plant']

print(f'My favorite plant is: {fav_plant}')

my_favorite_things['organism'] = 'human'
print(my_favorite_things)


for key in my_favorite_things:
	print(key, '=>', my_favorite_things[key])

new_thing = input(f'Please add your favorite item from this list:\nDance\nFood\nWine:\n')
new_value = input(f'Great! Now input your favorite {new_thing}:')

my_favorite_things[new_thing] = new_value

print('Cool, here is the new dictionary!:')
for key in my_favorite_things:
	print(key, '=>', my_favorite_things[key]) 


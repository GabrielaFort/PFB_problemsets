#!/usr/bin/env python3

print('This script will take two sets and will find the intersection, difference, union, and symmetrical difference between them')

Set_A = {3, 14, 15, 9, 26, 5, 35, 9}
Set_B = {60, 22, 14, 0, 9}

print(f'Original sets are: {Set_A} AND: {Set_B}')

intersection = Set_A & Set_B
difference_avsb = Set_A - Set_B
difference_bvsa = Set_B - Set_A
union = Set_A | Set_B
symmetrical_difference = Set_A ^ Set_B

print(f'The Intersection is:\n{intersection}\nThe difference of A vs B is:\n{difference_avsb}\nThe difference of B vs A is:\n{difference_bvsa}\nThe Union is:\n{union}\nThe Symmetrical Difference is:\n{symmetrical_difference}') 

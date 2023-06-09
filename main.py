razavi_children = ['Razie', 'Morteza', 'Mostafa', 'Pooskshooloo']

print('Total number of children:', len(razavi_children))


print('\nWithout loop (most stupid)')
print(razavi_children[0])
print(razavi_children[1])
print(razavi_children[2])
print(razavi_children[3])


print('\nUsing loop with index (not best)')
for i in range(len(razavi_children)):
    print(razavi_children[i])


print('\nUsing loop without index (best way)')
for child in razavi_children: 
    print(child)

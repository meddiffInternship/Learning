example=['red','green','blue','black','white']

for i,j in enumerate(example):
    print(i,j)

new_dict=dict(enumerate(example))
print(new_dict)

[print(i,j) for i,j in enumerate(new_dict)]

x=[3, 7, 5, 9]
y=[4.8, 9.5, 2.5, 6.6]
z=['left', 'right', 'up', 'down']

for a,b,c in zip(x,y,z):
    print(a,b,c)

for i in zip(x,y,z):
    print(i)

print(list(zip(x,y,z)))

[print(a,b) for a,b in zip(x,y)]

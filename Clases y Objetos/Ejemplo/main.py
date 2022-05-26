from Usuario import Usuario

user1 = Usuario("Rodrigo", "rodriale", "1234")

#print("Nombre: " + user1.getNombre())
#print("Username: " + user1.getUsername())
#print("Password: " + user1.getPassword())

usuarios = []

user2 = Usuario("Andres", "andrew123", "56789")

usuarios.append(user1)
usuarios.append(user2)

for i in range(len(usuarios)):
    print('----------------------------------')
    print("Nombre: " + usuarios[i].getNombre())
    print("Username: " + usuarios[i].getUsername())
    print("Password: " + usuarios[i].getPassword())
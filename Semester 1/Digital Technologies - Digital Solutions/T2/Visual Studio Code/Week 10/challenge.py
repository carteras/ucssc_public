def make_galaxy(name, distance, galaxy_type):
    distance = f'{distance} Million Light Years'

    if galaxy_type == 'S':
        galaxy_type == 'Spiral'
        name = '{name} galaxy'
    elif galaxy_type == "E":
        galaxy_type == "Elliptical"
        name = f'{name} Galaxy'
    elif galaxy_type == "I":
        galaxy_type == "Irregular"
    elif galaxy_type == 'L':
        galaxy_type == "Lenticular"
        name = f'{name} galaxy'
    
    return (name, distance, galaxy_type)

galaxies = []

galaxies.append(make_galaxy("Tadpole", 400, 'S'))
galaxies.append(make_galaxy('Pinwheel', 25, 'S'))
galaxies.append(make_galaxy('Cartwheel', 500, 'L'))
galaxies.append(make_galaxy('Andromeda', 3, 'S'))
galaxies.append(make_galaxy('Maffei 1', 11, 'E'))
galaxies.append(make_galaxy('Small Magellanic Cloud', 0.2, 'I'))

for galaxy in galaxies:
    name = galaxy[0]
    distance = galaxy[1]
    galaxy_type = galaxy[2]
    print(f'Hey, did you know that the {name} {distance} {galaxy_type}')
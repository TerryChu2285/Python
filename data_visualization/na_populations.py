import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 33247823, 'us': 32047723, 'mx': 321414})

wm.render_to_file('na_population.svg')

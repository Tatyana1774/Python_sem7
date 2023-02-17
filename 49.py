def find_facturhest_orbit(orbits):
    return max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (100, 100)]
print(*find_facturhest_orbit(orbits))
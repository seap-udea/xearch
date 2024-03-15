systems = {

    'Solar System' : dict(
        name = 'Solar System',
        units = 'Msun, Rsun, Mearth, Rearth, AU, days, deg',
        star = dict(
            mass = 1.989 * 10**30, # in solar masses
            radius = 6.9634 * 10**8, # in solar radii
        ),
        planets = [
            dict(
                name = 'Mercury',
                method = 'Transit',
                mass = 3.3011 * 10**23, # in Earth masses
                period = 87.97, # in days
                radius = 2.4397 * 10**6, # in Earth radii
                a = 0.387, # in AU
                e = 0.2056, # eccentricity
                I = 7.005, # deg, inclination
            ),
            dict(
                name = 'Venus',
                method = 'Transit',
                mass = 4.8675 * 10**24, # in Earth masses
                period = 224.7, # in days
                radius = 6.0518 * 10**6, # in Earth radii
                a = 0.723, # in AU
                e = 0.0068, # eccentricity
                I = 3.394, # deg, inclination
            ),
            dict(
                name = 'Earth',
                method = 'Transit',
                mass = 5.972 * 10**24, # in Earth masses
                period = 365.25, # in days
                radius = 6.371 * 10**6, # in Earth radii
                a = 1.0, # in AU
                e = 0.0167, # eccentricity
                I = 0.0, # deg, inclination
            ),
            dict(
                name = 'Mars',
                method = 'Transit',
                mass = 6.4171 * 10**23, # in Earth masses
                period = 686.97, # in days
                radius = 3.3895 * 10**6, # in Earth radii
                a = 1.524, # in AU
                e = 0.0934, # eccentricity
                I = 1.850, # deg, inclination
            ),
            dict(
                name = 'Jupiter',
                method = 'Transit',
                mass = 1.8982 * 10**27, # in Earth masses
                period = 4332.59, # in days
                radius = 6.9911 * 10**7, # in Earth radii
                a = 5.203, # in AU
                e = 0.0484, # eccentricity
                I = 1.305, # deg, inclination
            ),
            dict(
                name = 'Saturn',
                method = 'Transit',
                mass = 5.6834 * 10**26, # in Earth masses
                period = 10759.22, # in days
                radius = 5.8232 * 10**7, # in Earth radii
                a = 9.537, # in AU
                e = 0.0542, # eccentricity
                I = 2.485, # deg, inclination
            ),
            dict(
                name = 'Uranus',
                method = 'Transit',
                mass = 8.6810 * 10**25, # in Earth masses
                period = 30688.5, # in days
                radius = 2.5362 * 10**7, # in Earth radii
                a = 19.191, # in AU
                e = 0.0472, # eccentricity
                I = 0.772, # deg, inclination
            ),
            dict(
                name = 'Neptune',
                method = 'Transit',
                mass = 1.02413 * 10**26, # in Earth masses
                period = 60182, # in days
                radius = 2.4622 * 10**7, # in Earth radii
                a = 30.069, # in AU
                e = 0.0086, # eccentricity
                I = 1.769, # deg, inclination
            )
        ]
    ),

    '51 Peg' : dict(
        name = '51 Peg',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 1.06, # in solar masses
            radius = 1.15, # in solar radii
        ),
        planets = [
            dict(
                name = 'b',
                method = 'Radial Velocity',
                mass = 0.468, # in jupiter masses
                period = 4.23, # in days
                radius = 1.9, # in jupiter radii
                a = 0.052, # in AU
                e = 0.0, # eccentricity
                I = 0.0, # deg, inclination
            )
        ]
    ),

    'TRAPPIST-1' : dict(
        name = 'TRAPPIST-1',
        units = 'Msun, Rsun, Mearth, Rearth, AU, days, deg',
        star = dict(
            mass = 0.089, # in solar masses
            radius = 0.121, # in solar radii
        ),
        planets = [
            dict(
                name = 'b',
                method = 'Transit',
                mass = 1.017, # in Earth masses
                period = 1.51087637, # in days
                radius = 1.086, # in Earth radii
                a = 0.01111, # in AU
                e = 0.081, # eccentricity
                I = 89.65, # deg, inclination
            ),
            dict(
                name = 'c',
                method = 'Transit',
                mass = 1.156, # in Earth masses
                period = 2.421807, # in days
                radius = 1.056, # in Earth radii
                a = 0.01522, # in AU
                e = 0.083, # eccentricity
                I = 89.66, # deg, inclination
            ),
            dict(
                name = 'd',
                method = 'Transit',
                mass = 0.297, # in Earth masses
                period = 4.049610, # in days
                radius = 0.772, # in Earth radii
                a = 0.02144, # in AU
                e = 0.070, # eccentricity
                I = 89.63, # deg, inclination
            ),
            dict(
                name = 'e',
                method = 'Transit',
                mass = 0.772, # in Earth masses
                period = 6.099615, # in days
                radius = 0.918, # in Earth radii
                a = 0.02817, # in AU
                e = 0.085, # eccentricity
                I = 89.64, # deg, inclination
            ),
            dict(
                name = 'f',
                method = 'Transit',
                mass = 0.934, # in Earth masses
                period = 9.206690, # in days
                radius = 1.045, # in Earth radii
                a = 0.03711, # in AU
                e = 0.064, # eccentricity
                I = 89.63, # deg, inclination
            ),
            dict(
                name = 'g',
                method = 'Transit',
                mass = 1.148, # in Earth masses
                period = 12.35294, # in days
                radius = 1.127, # in Earth radii
                a = 0.04510, # in AU
                e = 0.070, # eccentricity
                I = 89.63, # deg, inclination
            ),
            dict(
                name = 'h',
                method = 'Transit',
                mass = 0.331, # in Earth masses
                period = 18.767953, # in days
                radius = 0.755, # in Earth radii
                a = 0.05811, # in AU
                e = 0.085, # eccentricity
                I = 89.63, # deg, inclination
            )
        ]
    ),

    # Small planets
    'Proxima Centauri' : dict(
        name = 'Proxima Centauri',
        units = 'Msun, Rsun, Mearth, Rearth, AU, days, deg',
        star = dict(
            mass = 0.1221, # in solar masses
            radius = 0.1542, # in solar radii
        ),
        planets = [
            dict(
                name = 'b',
                method = 'Radial Velocity',
                mass = 1.07, # in Earth masses
                period = 11.186, # in days
                radius = 1.30, # in Earth radii
                a = 0.0485, # in AU
                e = 0.109, # eccentricity
                I = 0.0, # deg, inclination
            ),
            dict(
                name = 'c',
                method = 'Radial Velocity',
                mass = 7.0, # in Earth masses
                period = 1928.0, # in days
                radius = None, # in Earth radii
                a = 1.489, # in AU
                e = 0.04, # eccentricity
                I = 0.0, # deg, inclination
            ),
            dict(
                name = 'd',
                method = 'Radial Velocity',
                mass = 0.26, # in Earth masses
                period = 5.122, # in days
                radius = 0.81, # in Earth radii
                a = 0.02885, # in AU
                e = 0.04, # eccentricity
                I = 0.0, # deg, inclination
            )
        ]
    ),

    'GJ3512' : dict(
        name = 'GJ3512',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 0.123, # in solar masses
            radius = 0.139, # in solar radii
        ),
        planets = [
            dict(
            name = 'b',
            method = 'Radial Velocity',
            mass = 0.46, # in jupiter masses
            period = 204.7, # in days
            radius = 1.0, # in jupiter radii
            a = 0.3380, # in AU
            e = 0.4356, # eccentricity
            I = 0.0, # deg, inclination
            ),
        ]
    ),

    'HD 89744' : dict(
        name = 'HD 89744',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 1.37, # in solar masses
            radius = 2.16, # in solar radii
        ),
        planets = [
            dict(
                name = 'b',
                method = 'Radial Velocity',
                mass = 7.99, # in jupiter masses
                period = 256.605, # in days
                radius = None, # in jupiter radii
                a = 0.89, # in AU
                e = 0.67, # eccentricity
                I = 0.0, # deg, inclination
            ),
        ]
    ),

    # Planetary system with perturbations
    'Upsilon Andromedae' : dict(
        name = 'Upsilon Andromedae',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 1.27, # in solar masses
            radius = 1.48, # in solar radii
        ),
        planets = [
            dict(
                name = 'b',
                method = 'Radial Velocity',
                mass = 1.70, # in jupiter masses
                period = 4.617, # in days
                radius = None, # in jupiter radii
                a = 0.059, # in AU
                e = 0.021, # eccentricity
                I = 24, # deg, inclination
            ),
            dict(
                name = 'c',
                method = 'Radial Velocity',
                mass = 13.98, # in jupiter masses
                period = 241.3, # in days
                radius = None, # in jupiter radii
                a = 0.830, # in AU
                e = 0.260, # eccentricity
                I = 7.9, # deg, inclination
            ),
            dict(
                name = 'd',
                method = 'Radial Velocity',
                mass = 10.25, # in jupiter masses
                period = 1276, # in days
                radius = None, # in jupiter radii
                a = 2.53, # in AU
                e = 0.298, # eccentricity
                I = 23.8, # deg, inclination
            ),
        ]
    ),

}

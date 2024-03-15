systems = {
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

    'eps And' : dict(
        name = 'Epsilon Andromedae',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 2.2, # in solar masses
            radius = 1.8, # in solar radii
        ),
        planets = [
            dict(
                method = 'Radial Velocity',
                mass = 1.17, # in jupiter masses
                period = 4.62, # in days
                radius = 1.56, # in jupiter radii
                a = 0.059, # in AU
                e = 0.0, # eccentricity
                I = 30.0, # deg, inclination
            ),
            dict(
                method = 'Radial Velocity',
                mass = 0.77, # in jupiter masses
                period = 241.3, # in days
                radius = 1.17, # in jupiter radii
                a = 0.83, # in AU
                e = 0.0, # eccentricity
                I = 30.0, # deg, inclination
            ),
            dict(
                method = 'Radial Velocity',
                mass = 0.69, # in jupiter masses
                period = 1246.0, # in days
                radius = 1.25, # in jupiter radii
                a = 2.51, # in AU
                e = 0.0, # eccentricity
                I = 30.0, # deg, inclination
            ),
            dict(
                method = 'Radial Velocity',
                mass = 1.76, # in jupiter masses
                period = 1237.0, # in days
                radius = 1.08, # in jupiter radii
                a = 3.49, # in AU
                e = 0.0, # eccentricity
                I = 30.0, # deg, inclination
            )
        ]
    ),

    'Kepler 11': dict(
        name = 'Kepler-11',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 1.9, # in solar masses
            radius = 1.5, # in solar radii
        ),
        planets = [
            dict(
                method = 'Transit',
                mass = 0.006, # in jupiter masses
                period = 10.303, # in days
                radius = 0.26, # in jupiter radii
                a = 0.091, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.009, # in jupiter masses
                period = 13.024, # in days
                radius = 0.37, # in jupiter radii
                a = 0.106, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.023, # in jupiter masses
                period = 22.684, # in days
                radius = 0.46, # in jupiter radii
                a = 0.158, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.047, # in jupiter masses
                period = 46.688, # in days
                radius = 0.57, # in jupiter radii
                a = 0.224, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.071, # in jupiter masses
                period = 77.612, # in days
                radius = 0.73, # in jupiter radii
                a = 0.296, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.166, # in jupiter masses
                period = 118.377, # in days
                radius = 0.95, # in jupiter radii
                a = 0.464, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            )
        ]
    ),

    'Trappist-1' : dict(
        name = 'TRAPPIST-1',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 0.08, # in solar masses
            radius = 0.12, # in solar radii
        ),
        planets = [
            dict(
                method = 'Transit',
                mass = 0.85, # in earth masses
                period = 1.51, # in days
                radius = 1.09, # in earth radii
                a = 0.028, # in AU
                e = 0.0, # eccentricity
                I = 89.65, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 1.38, # in earth masses
                period = 2.42, # in days
                radius = 1.06, # in earth radii
                a = 0.037, # in AU
                e = 0.0, # eccentricity
                I = 89.66, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.41, # in earth masses
                period = 4.05, # in days
                radius = 0.77, # in earth radii
                a = 0.045, # in AU
                e = 0.0, # eccentricity
                I = 89.63, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.62, # in earth masses
                period = 6.10, # in days
                radius = 0.91, # in earth radii
                a = 0.056, # in AU
                e = 0.0, # eccentricity
                I = 89.64, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.68, # in earth masses
                period = 9.21, # in days
                radius = 1.05, # in earth radii
                a = 0.073, # in AU
                e = 0.0, # eccentricity
                I = 89.64, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 1.34, # in earth masses
                period = 12.35, # in days
                radius = 1.13, # in earth radii
                a = 0.095, # in AU
                e = 0.0, # eccentricity
                I = 89.64, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.33, # in earth masses
                period = 18.77, # in days
                radius = 0.77, # in earth radii
                a = 0.128, # in AU
                e = 0.0, # eccentricity
                I = 89.64, # deg, inclination
            )
        ]
    ),

    'HD209458' : dict(
        name = 'HD 209458',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 1.1, # in solar masses
            radius = 1.2, # in solar radii
        ),
        planets = [
            dict(
                method = 'Transit',
                mass = 0.69, # in jupiter masses
                period = 3.52474859, # in days
                radius = 1.38, # in jupiter radii
                a = 0.0475, # in AU
                e = 0.0, # eccentricity
                I = 86.7, # deg, inclination
            ),
            dict(
                method = 'Radial Velocity',
                mass = 0.69, # in jupiter masses
                period = 3.52474859, # in days
                radius = 1.38, # in jupiter radii
                a = 0.0475, # in AU
                e = 0.0, # eccentricity
                I = 86.7, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.69, # in jupiter masses
                period = 3.52474859, # in days
                radius = 1.38, # in jupiter radii
                a = 0.0475, # in AU
                e = 0.0, # eccentricity
                I = 86.7, # deg, inclination
            )
        ]
    ),
    
    'Solar System' : dict(
        name = 'Solar System',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 1.0, # in solar masses
            radius = 1.0, # in solar radii
        ),
        planets = [
            dict(
                method = 'N/A',
                mass = 0.000003, # in jupiter masses
                period = 0.2408467, # in days
                radius = 0.3829, # in jupiter radii
                a = 0.387, # in AU
                e = 0.2056, # eccentricity
                I = 7.005, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.00095, # in jupiter masses
                period = 0.61519726, # in days
                radius = 0.9499, # in jupiter radii
                a = 0.723, # in AU
                e = 0.0068, # eccentricity
                I = 3.39471, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.000285, # in jupiter masses
                period = 1.0000174, # in days
                radius = 1.0, # in jupiter radii
                a = 1.0, # in AU
                e = 0.0167, # eccentricity
                I = 0.0, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.000043, # in jupiter masses
                period = 1.8808476, # in days
                radius = 0.532, # in jupiter radii
                a = 1.524, # in AU
                e = 0.0934, # eccentricity
                I = 1.85061, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.051, # in jupiter masses
                period = 11.862615, # in days
                radius = 11.209, # in jupiter radii
                a = 5.203, # in AU
                e = 0.0484, # eccentricity
                I = 1.3053, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.045, # in jupiter masses
                period = 29.447498, # in days
                radius = 9.4492, # in jupiter radii
                a = 9.582, # in AU
                e = 0.0565, # eccentricity
                I = 2.48446, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.000051, # in jupiter masses
                period = 84.016846, # in days
                radius = 4.007, # in jupiter radii
                a = 19.189, # in AU
                e = 0.0464, # eccentricity
                I = 0.76986, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.000023, # in jupiter masses
                period = 164.79132, # in days
                radius = 3.883, # in jupiter radii
                a = 30.069, # in AU
                e = 0.0095, # eccentricity
                I = 1.76917, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.000003, # in jupiter masses
                period = 248.54, # in days
                radius = 0.186, # in jupiter radii
                a = 39.482, # in AU
                e = 0.2488, # eccentricity
                I = 17.14175, # deg, inclination
            ),
            dict(
                method = 'N/A',
                mass = 0.0000002, # in jupiter masses
                period = 247.94, # in days
                radius = 0.159, # in jupiter radii
                a = 39.445, # in AU
                e = 0.2488, # eccentricity
                I = 16.812, # deg, inclination
            )
        ]
    ),

    'Kepler-22' : dict(
        name = 'Kepler-22',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 0.97, # in solar masses
            radius = 0.97, # in solar radii
        ),
        planets = [
            dict(
                method = 'Transit',
                mass = 0.181, # in jupiter masses
                period = 289.862, # in days
                radius = 2.35, # in jupiter radii
                a = 0.849, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.036, # in jupiter masses
                period = 122.387, # in days
                radius = 0.87, # in jupiter radii
                a = 0.374, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.078, # in jupiter masses
                period = 49.514, # in days
                radius = 1.38, # in jupiter radii
                a = 0.253, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.071, # in jupiter masses
                period = 19.378, # in days
                radius = 1.29, # in jupiter radii
                a = 0.117, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.071, # in jupiter masses
                period = 19.378, # in days
                radius = 1.29, # in jupiter radii
                a = 0.117, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.071, # in jupiter masses
                period = 19.378, # in days
                radius = 1.29, # in jupiter radii
                a = 0.117, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            ),
            dict(
                method = 'Transit',
                mass = 0.071, # in jupiter masses
                period = 19.378, # in days
                radius = 1.29, # in jupiter radii
                a = 0.117, # in AU
                e = 0.0, # eccentricity
                I = 89.8, # deg, inclination
            )
        ]
    ),

    'Proxima' : dict(
        name = 'Proxima',
        units = 'Msun, Rsun, Mjup, Rjup, AU, days, deg',
        star = dict(
            mass = 0.12, # in solar masses
            radius = 0.14, # in solar radii
        ),
        planets = [
            dict(
                method = 'Radial Velocity',
                mass = 0.003, # in jupiter masses
                period = 11.186, # in days
                radius = 0.146, # in jupiter radii
                a = 0.0485, # in AU
                e = 0.0, # eccentricity
                I = 90.0, # deg, inclination
            )
        ]
    ),

}

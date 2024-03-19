systems = {
    'Solar System' : dict(
        name = 'Solar System',
        star = dict(
            mass = 1, # in solar masses
            radius = 1, # in solar radii
        ),
        planets = [
            dict(
                name = 'Jupiter',
                method = 'Transit',
                mass = 317.83, # in Earth masses
                radius = 10.973, # in Earth radii, volumetric radius
                period = 4332.59, # in days
                a = 5.203, # in AU
                e = 0.0484, # eccentricity
                I = 1.305, # deg, inclination
                W = 14.75, # deg, longitude of ascending node
                w = 100.55615, # deg, argument of periastron
                M = 34.40438, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Mercury',
                method = 'Transit',
                mass = 0.0553, # in Earth masses
                radius = 0.3829, # in Earth radii, volumetric radius
                period = 87.969, # in days
                a = 0.387, # in AU
                e = 0.2056, # eccentricity
                I = 7.004, # deg, inclination
                W = 48.331, # deg, longitude of ascending node
                w = 29.124, # deg, argument of periastron
                M = 174.796, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Venus',
                method = 'Transit',
                mass = 0.815, # in Earth masses
                radius = 0.9499, # in Earth radii, volumetric radius
                period = 224.701, # in days
                a = 0.723, # in AU
                e = 0.0068, # eccentricity
                I = 3.394, # deg, inclination
                W = 76.680, # deg, longitude of ascending node
                w = 54.884, # deg, argument of periastron
                M = 50.115, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Earth',
                method = 'Transit',
                mass = 1, # in Earth masses
                radius = 1, # in Earth radii, volumetric radius
                period = 365.256, # in days
                a = 1, # in AU
                e = 0.0167, # eccentricity
                I = 0, # deg, inclination
                W = 0, # deg, longitude of ascending node
                w = 102.937, # deg, argument of periastron
                M = 358.617, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Mars',
                method = 'Transit',
                mass = 0.107, # in Earth masses
                radius = 0.532, # in Earth radii, volumetric radius
                period = 686.971, # in days
                a = 1.524, # in AU
                e = 0.0934, # eccentricity
                I = 1.850, # deg, inclination
                W = 49.562, # deg, longitude of ascending node
                w = 286.537, # deg, argument of periastron
                M = 19.373, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Jupiter',
                method = 'Transit',
                mass = 317.83, # in Earth masses
                radius = 10.973, # in Earth radii, volumetric radius
                period = 4332.59, # in days
                a = 5.203, # in AU
                e = 0.0484, # eccentricity
                I = 1.305, # deg, inclination
                W = 14.75, # deg, longitude of ascending node
                w = 100.55615, # deg, argument of periastron
                M = 34.40438, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Saturn',
                method = 'Transit',
                mass = 95.162, # in Earth masses
                radius = 9.4492, # in Earth radii, volumetric radius
                period = 10759.22, # in days
                a = 9.537, # in AU
                e = 0.0542, # eccentricity
                I = 2.484, # deg, inclination
                W = 92.431, # deg, longitude of ascending node
                w = 336.041, # deg, argument of periastron
                M = 50.115, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Uranus',
                method = 'Transit',
                mass = 14.536, # in Earth masses
                radius = 4.007, # in Earth radii, volumetric radius
                period = 30688.5, # in days
                a = 19.191, # in AU
                e = 0.0472, # eccentricity
                I = 0.772, # deg, inclination
                W = 170.964, # deg, longitude of ascending node
                w = 96.998857, # deg, argument of periastron
                M = 314.055, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Neptune',
                method = 'Transit',
                mass = 17.147, # in Earth masses
                radius = 3.883, # in Earth radii, volumetric radius
                period = 60182, # in days
                a = 30.069, # in AU
                e = 0.0086, # eccentricity
                I = 1.769, # deg, inclination
                W = 44.971, # deg, longitude of ascending node
                w = 276.336, # deg, argument of periastron
                M = 304.880, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
            dict(
                name = 'Pluto',
                method = 'Transit',
                mass = 0.00218, # in Earth masses
                radius = 0.186, # in Earth radii, volumetric radius
                period = 90560, # in days
                a = 39.482, # in AU
                e = 0.2488, # eccentricity
                I = 17.140, # deg, inclination
                W = 110.303, # deg, longitude of ascending node
                w = 113.763, # deg, argument of periastron
                M = 238.965, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            ),
        ]
    ),

    '51 Peg' : dict(
        name = '51 Peg',
        star = dict(
            mass = 1.06, # in solar masses
            radius = 1.15, # in solar radii
        ),
        planets = [
            dict(
                name = 'b',
                proper = 'Dimidium',
                method = 'Radial Velocity',
                mass = 179.16, # in jupiter masses
                period = 4.23, # in days
                radius = 21.28, # in jupiter radii
                a = 0.052, # in AU
                e = 0.0, # eccentricity
                I = 0.0, # deg, inclination
                W = 0.0, # deg, longitude of ascending node
                w = 0.0, # deg, argument of periastron
                M = 0.0, # deg, mean anomaly
                epoch = 2451545.0, # Julian date, J2000
            )
        ]
    ),
    
}

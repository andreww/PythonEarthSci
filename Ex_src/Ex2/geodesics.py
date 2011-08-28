#!/usr/bin/env python

import math as m

def vincenty(lat1, lon1, lat2, lon2,
            r_major=6378.1370, r_minor=6356.752314, r_sphere=None):
    """
    Vincenty's method for distances on the globe (usually overkill)

    Calculates the distance and direction between two points on an
    ellipsoid using Vincenty's inverse approach (T. Vincenty 1975,
    "Direct and inverse solutions of geodesics on the ellipsoid with
    application of nested equations" Survey Review XXII pp.88-93).
 
    Arguments are the lattitude and longitude of the two points (in
    degrees) and, optionally, the semi-major and semi-minor radius of the
    ellipsoid or the radius of a sphere (if polar flattening is ignored).
    These default to the WGS 84 ellipsoid. Changing the units of the
    radii changes the units of the resultant distance, but note that the
    other arguments should always be in degrees.
 
    A length three tuple is returned. The first element is the distance
    between the two points, the second and third are the azimuths of the
    geodesic in degrees clockwise from north.

    """
    lat1 = m.radians(lat1)
    lat2 = m.radians(lat2)
    lon1 = m.radians(lon1)
    lon2 = m.radians(lon2)
 
    if (r_sphere is not None):
        r_major = r_sphere
        r_minor = r_sphere
        f = 0.0
    else:
        f = (r_major-r_minor)/r_major
 
    U1 = m.atan((1.0-f) * m.tan(lat1))
    U2 = m.atan((1.0-f) * m.tan(lat2))
    L = lon2 - lon1
 
    epsilon = 1E-12 # Accuracy (10E-12 -> ~ 0.06mm)
    max_iter = 500
    lam = L
 
    cU1 = m.cos(U1)
    cU2 = m.cos(U2)
    sU1 = m.sin(U1)
    sU2 = m.sin(U2)
 
    for i in range(max_iter):
        lam_old = lam
        sLam = m.sin(lam)
        cLam = m.cos(lam)
        sin_sig = m.sqrt((cU2*sLam)**2 + (cU1*sU2 - sU1*cU2*cLam)**2)
        cos_sig = sU1*sU2 + cU1*cU2*cLam
        sig = m.atan2(sin_sig,cos_sig)
        sin_alp = (cU1*cU2*sLam) / sin_sig
        cos2_alp = 1.0 - sin_alp**2
        if (cos2_alp == 0.0):
            # equitorial line
            cos_2sigm = 100
            C = 0.0
        else:
            cos_2sigm = cos_sig - (2.0*sU1*sU2)/cos2_alp
            C = f/16.0 * cos2_alp * (4.0 + f*(4.0-3.0*cos2_alp))
        lam = L + (1.0 - C) * f * sin_alp * \
            (sig + C * sin_sig * (cos_2sigm + C * cos_sig * \
            (-1.0 + 2.0 * cos_2sigm**2)))
        if ((m.fabs(lam - lam_old)) <= epsilon):
            # Found a solution in i iters...
            break
        elif (i == max_iter):
            # Catch the out of iters case, never seen this.
            raise Exception("Failed to solve for distance")
 
    usq = cos2_alp * ((r_major**2 - r_minor**2) / r_minor**2)
    A = 1 + usq/16384 * (4096 + usq*(-768 + usq*(320 - 175*usq)))
    B = usq/1024 * (256 + usq*(-128 + usq*(74 - 47*usq)))
    del_sig = B * sin_sig * (cos_2sigm + 0.25*B*(cos_sig*( \
        -1 + 2*cos_2sigm**2) - (1.0/6.0)*B*cos_2sigm * ( \
        -3 + 4*sin_sig**2) * (-3 + 4 * cos_2sigm**2)))
    s = r_minor * A * (sig - del_sig)
    alp1 = m.atan2(cU2*m.sin(lam),(cU1*sU2-sU1*cU2*m.cos(lam)))
    alp2 = m.atan2(cU1*m.sin(lam),(cU1*sU2*m.cos(lam)-sU1*cU2))

    return (s, m.degrees(alp1), m.degrees(alp2))

if __name__ == "__main__":
    import sys
    print "Latitude / longitude, point 1: " + sys.argv[1] + " / " + sys.argv[2]
    print "Latitude / longitude, point 2: " + sys.argv[3] + " / " + sys.argv[4]
    (distance, geodesic1, geodesic2) = vincenty(float(sys.argv[1]), 
        float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    print "Distance (Vincenty's method), km: " + str(distance)

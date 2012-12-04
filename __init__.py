"""Some alternative units expressed in their SI counterparts.

This only provides scaling factors.
The idea is to scale manually with no units overhead. 

This is for convenience only. For a more complete standard package,
consider e.g. sympy.physics.units 
"""

# time (in seconds)
ms = 1e-3 # [s] millisecond
us = 1e-6 # [s] microsecond
ns = 1e-9 # [s] nanosecond
ps = 1e-12 # [s] picosecond
minute = 60. # [s] minute ('min' is for minimum)
h = hr = hour = 3600. # [s] hour
day = 86400. # [s] day
week = 7 * day # [s] week
yr = year = 365.25 * day # [s] year
mo = month = yr / 12. # [s] average month

# length (in meters)
inch = 0.0254 # [m] inch  ('in' is a reserved word)
ft = foot = 0.3048 # [m] foot
mm = 1e-3 # [m] millimeter
cm = 1e-2 # [m] centimeter
km = 1e3 # [m] kilometer

# mass (in kilograms)
amu = 1.66053886e-27 # [kg] atomic mass unit 
lb = pound = 0.45359237 # [kg] pound

# energy (in joules)
eV = 1.60217646e-19 # [J] electron volt
keV = 1.60217646e-16 # [J] kilo-electron volt
MeV = 1.60217646e-13 # [J] mega-electron volt
GeV = 1.60217646e-10 # [J] giga-electron volt

# pressure (in pascals)
Torr = 101325. / 760. # [Pa] Torr (approx. 133.3224 Pa)
bar = 1e5 # [Pa] bar
mbar = 100. # [Pa] millibar

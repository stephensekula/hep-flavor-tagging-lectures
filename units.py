# Conversion Factors
import math

# distance
_m=1
_km=1000*_m
_cm=_m/100
_mm=_m/1000.
_in=2.54*_cm
_ft=12*_in
_mile=5280*_ft
_miles=_mile
_ly=9460730472580800*_m
_Angstrom=1e-10*_m


# time
_s=1
_ms=_s/1000
_mus=_s/1e6
_min=60*_s
_hour=60*_min
_hours=_hour
_day=24*_hours
_days=_day
_year=365.25*_days
_years=_year
_year_approx=365*_days

# mass
_kg=1
_g=_kg/1000
_lb=_kg/2.2
_oz=(1/16)*_lb
_amu = 1.66053886e-27*_kg

# charge
_C = 1.602e-19 # couloumb

# Force
_N = _kg*_m/_s**2
_dyn = 1e-5*_N

# Energy
_J = _N*_m
_W = _J/_s

_eV = _J*_C
_keV = 1e3*_eV
_MeV = 1e6*_eV
_GeV = 1e9*_eV
_TeV = 1e12*_eV


# Temperature

_K = 1
_Celsius = _K

# Angles
_rad=1
_deg=math.pi/180*_rad

# Constants of nature
_c = 2.998e8 * _m/_s
_h = 6.626e-34 * _kg*_m/_s
_hbar = _h/(2*math.pi)
_G = 6.67408e-11 * _N*_m**2/_kg**2



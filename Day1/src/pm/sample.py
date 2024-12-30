# targets between Sun distance unit AU
destinations_dict = {
    "Sun": 0,
    "Earth": 1.0,
    "Mars": 2.52,
    "Jupiter": 5.2,
    "Pluto": 40.5
}

# 1AU = 149600000km
CONSTANT_KM_ONE_AU = 149600000

if __name__ == '__main__':
    keys = destinations_dict.keys()
    print(keys)

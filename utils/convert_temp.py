def convert_temp(kelvin: float):
    try:
        return round(kelvin - 273.15, 2)
    except Exception as e:
        print(e)
        
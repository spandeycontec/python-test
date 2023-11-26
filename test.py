def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif temperature >0 and temperature <100:
        return "Liquid"
    elif temperature >= 100:
        return "Gas"
    
    
print(water_state(0))
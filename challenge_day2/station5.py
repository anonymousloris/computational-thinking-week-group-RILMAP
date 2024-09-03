def solution_station_1():
    names = ["Kimiya", "Tadas", "Anouk"]

    def custom_rule(name):
        
        unique_letters = set(name.lower())
        return len(unique_letters)  

    outputs = [custom_rule(name) for name in names]
    return outputs

print(solution_station_1())

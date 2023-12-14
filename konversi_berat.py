def kg_to_lbs(weight_kg):
    # 1 kg = 2.20462 lbs
    weight_lbs = weight_kg * 2.20462
    return weight_lbs

def lbs_to_kg(weight_lbs):
    # 1 lbs = 0.453592 kg
    weight_kg = weight_lbs * 0.453592
    return weight_kg

# Input dari pengguna
unit = input("Masukkan unit berat (kg atau lbs): ").lower()

if unit == 'kg':
    weight_input = float(input("Masukkan berat dalam kilogram: "))
    weight_output = kg_to_lbs(weight_input)
    print(f"{weight_input} kg sama dengan {weight_output:.2f} lbs")
elif unit == 'lbs':
    weight_input = float(input("Masukkan berat dalam pound: "))
    weight_output = lbs_to_kg(weight_input)
    print(f"{weight_input} lbs sama dengan {weight_output:.2f} kg")
else:
    print("Unit berat yang dimasukkan tidak valid. Harap masukkan 'kg' atau 'lbs'.")
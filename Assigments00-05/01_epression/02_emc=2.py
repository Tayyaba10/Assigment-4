"""
Write a program that continually reads in mass from the user 
and then outputs the equivalent energy using Einstein's mass-energy 
equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
"""

# use a constant value for the speed of light 
C = 299792458 

def main():
    mass_in_kg = float(input("\033[1;3m Enter kilos of mass:\033[0m"))
    
    # calculate energy using mass-energy equivalence formula
    energy_in_joule = mass_in_kg * (C ** 2)

    #Display work to the user
    print("e = m * C^2...")

    print(f"m = {mass_in_kg} kg")

    print(f"C = {C} m/s")

    print(f"{energy_in_joule} joules of energy!")


if __name__ == '__main__':
    main()
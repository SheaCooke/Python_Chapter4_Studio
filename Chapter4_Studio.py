date = "Monday 2019-03-18"

time = "10:05:34 AM"

average_astronaut_mass_kg = 80.7

fuel_mass_kg = 760000

ship_mass_kg = 74842.31

fuel_level = "100%"

num_astronauts_in_crew = int(input("Enter number of astronauts in crew: "))

crew_status = input("Enter crew status, Ready or Not Ready: ")

total_mass_of_crew = num_astronauts_in_crew * average_astronaut_mass_kg

total_mass_of_ship = total_mass_of_crew + ship_mass_kg + fuel_mass_kg

dashes = "-------------------"

print(f"> LAUNCH CHECKLIST\n{dashes}\nDate: {date}\nTime: {time}\n\n{dashes}\n> SHIP INFO\n{dashes}")
      
print(f"* Crew: {num_astronauts_in_crew}\n* Crew Status: {crew_status}\n* Fuel Level: {fuel_level}\n\n")
      
print(f"{dashes}\n> MASS DATA\n{dashes}\n* Crew: {total_mass_of_crew} kg\n* Fuel: {fuel_mass_kg} kg")
print(f"* Spaceship: {ship_mass_kg} kg\n* Total Mass: {total_mass_of_ship} kg")




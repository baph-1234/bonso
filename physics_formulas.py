print("PHYSICS FORMULA CALCULATOR")
print("Choose a formula to calculate:")
print("a. Speed = Distance / Time")
print("b. Force = Mass × Acceleration")
print("c. Density = Mass / Volume")
print("d. Pressure = Force / Area")
print("e. Work = Force × Distance")

choice = input("Enter the letter of the formula you want (a-e): ").strip().lower()

if choice == 'a':
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    if time != 0:
        speed = distance / time
        print("Speed =", speed, "m/s")
    else:
        print("Time cannot be zero.")
elif choice == 'b':
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    force = mass * acceleration
    print("Force =", force, "N")
elif choice == 'c':
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m^3): "))
    if volume != 0:
        density = mass / volume
        print("Density =", density, "kg/m^3")
    else:
        print("Volume cannot be zero.")
elif choice == 'd':
    force = float(input("Enter force (N): "))
    area = float(input("Enter area (m^2): "))
    if area != 0:
        pressure = force / area
        print("Pressure =", pressure, "Pa")
    else:
        print("Area cannot be zero.")
elif choice == 'e':
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    work = force * distance
    print("Work =", work, "J")
else:
    print("Invalid choice. Please select a letter from a to e.")

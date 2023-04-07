# This program finds the surface area and volume of a 3D box.

def main():
    # Set the variables height, width, and length to their input values.
    height = float(input("Enter the height of the box in inches: "))
    width = float(input("Enter the width of the box in inches: "))
    length = float(input("Enter the length of the box in inches: "))

    # Surface area, volume, and feet equations.
    surface_area, volume = box_properties(height, width, length)
    height_ft, height_in = divmod(height, 12)
    width_ft, width_in = divmod(width, 12)
    length_ft, length_in = divmod(length, 12)

    # Display the surface area and the volume of box in sq. in and cubic in.
    print(f"\nSurface area of the box: {surface_area} square inches")
    print(f"Volume of the box: {volume} cubic inches\n")

    # Display the height, width, and length of the box in ft and in.
    print(f"The height of the box is: {int(height_ft)} ft {height_in} in")
    print(f"The width of the box is: {int(width_ft)} ft {width_in} in")
    print(f"The length of the box is: {int(length_ft)} ft {length_in} in")

def box_properties(height, width, length):
    # Surface areas and volume equations
    surface_area = 2 * (height * width) + 2 * (height * length) + 2 * (width * length)
    volume = height * width * length
    return surface_area, volume

main()

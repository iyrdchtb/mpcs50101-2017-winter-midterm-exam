# Problem 5:  How many ping pong balls can fit inside a Boeing 747 airplane?
#
# Use the following information to answer the question:
#   - The radius of a ping pong ball is .02 meters
#   - The volume of an Boeing 747 airplane is 1035 cubic meters
#   - The formula for the volume of a sphere is (4/3) * pi * radius^3
#
# In your solution, define and write a function named `volume_of_sphere` that
# takes a single parameter named `radius` returns the volume.
#
# Write the remainder of the program that calls the function.  Print your final
# answer out.
#
# If you have time, please let us know where you see yourself in 5 years :)
#
# Problem 5:  How many ping pong balls can fit inside a Boeing 747 airplane?
#
# Use the following information to answer the question:
#   - The radius of a ping pong ball is .02 meters
#   - The volume of an Boeing 747 airplane is 1035 cubic meters
#   - The formula for the volume of a sphere is (4/3) * pi * radius^3
#
# In your solution, define and write a function named `volume_of_sphere` that
# takes a single parameter named `radius` returns the volume.
#
# Write the remainder of the program that calls the function.  Print your final
# answer out.
#
# If you have time, please let us know where you see yourself in 5 years :)
#


def volume_of_sphere(radius):
    volume = (4/3)*3.14159*(pow(radius,3))
    return volume

print "We know that The radius of a ping pong ball is .02 meters"
print "The volume of an Boeing 747 airplane is 1035 cubic meters"
print "The formula for the volume of a sphere is (4/3) * pi * radius^3"

ball_radius = .02
ball_volume = volume_of_sphere(ball_radius)
plane_volume = 1035
ball_count = plane_volume/ball_volume

print "Number of balls %d"%(ball_count)

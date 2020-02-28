# EDX.ORG
# Numpy

# height and weight are available as a regular lists

height = ( 8, 9, 7.5)
weight = (150, 160, 145)


# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg 
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

# 2D arrays
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2],
            [180, 90.0]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

# baseball is available as a regular list of lists

# Print out the 4th row of np_baseball
print(np_baseball[3,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 3rd player
print(np_baseball[2,0])
# Print out average height of player 
print(np.mean(np_baseball[:,0]))
# PRint out correlation between height an weight
print(np.corrcoef(np_baseball[:,0], np_baseball[:,1]))
# Print out all player with 180 height



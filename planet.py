# your all planet weight

planetry_weight_constants = {
   "Mercury" : 37.6,
   "Mars" : 37.8,
   "Jupiter": 236.0,
   "Saturn" : 108.1,
   "Uranus" : 81.5,
   "Neptune" : 114.0,
   "venus" : 88.9

} 

def planetary_weight():
   earth_weight = float(input("enter your earth weight plz: "))
   planet_of_choice = str(input("enter the name of planet you are going to visit: "))
   if planet_of_choice in planetry_weight_constants:
      planetary_weight = earth_weight * planetry_weight_constants[planet_of_choice] /100
      print(f"your weight on planet {planet_of_choice} is {planetary_weight}." )

   else:
    print("we can only calculate solar system values.")  

planetary_weight()


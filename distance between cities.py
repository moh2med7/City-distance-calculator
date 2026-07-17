from pystyle import *
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Initialize the geolocator with a user agent
geolocator = Nominatim(user_agent="city_distance_calculator")

# Display the program title and description
print(Box.Lines("[+] Distance Calculator [+]"))
Write.Print("[-] this program for distance between cities \n" , Colors.purple_to_red , interval=0.1)

try:
    # Get city names from the user
    city1_name = input(" Enter the first city name: ")
    city2_name = input(" Enter the second city name: ")

    # Fetch location detailes and coordinates for both cities
    location1 = geolocator.geocode(city1_name , language="en")
    location2 = geolocator.geocode(city2_name , language="en")

    # check if either of the locations is None (not found)
    if location1 is None or location2 is None:
        Write.Print("[-] One or both cities not found. Please check the names and try again.\n", Colors.red, interval=0.1)
    # check if both cities are the same    
    elif location1 == location2:
        Write.Print("[-] Both cities are the same. Please enter different cities.\n", Colors.red, interval=0.1)
    # If both locations are valid and different, calculate the distance
    elif location1 and location2:
        # Store the coordinates of both locations as (latitude, longitude) tuples
        f_p = (location1.latitude, location1.longitude)
        s_p = (location2.latitude, location2.longitude)
        # Calculate the distance in kilometers using geodesic
        dis = int(geodesic(f_p, s_p).km)
        # Extract the city names from the full address for display
        name1 = location1.address.split(',')[0]
        name2 = location2.address.split(',')[0]
        # Display the visual destination box with the city names
        print(Box.DoubleCube(f"From: {name1}  to  {name2}  "))
        # Round the coordinates to 4 decimal places for better readability
        lat1, lon1 = round(location1.latitude, 4), round(location1.longitude, 4)
        lat2, lon2 = round(location2.latitude, 4), round(location2.longitude, 4)
        # Print coordinates of both cities side-by-side with their names
        Write.Print(f'\n[i] Coordinates:\n', Colors.yellow_to_red, interval=0.1)
        print(f"\t - {name1} ({lat1}, {lon1})")
        print(f"\t - {name2} ({lat2}, {lon2})")
        # Print the final calculated distance between the two cities in kilometers
        Write.Print(f"[-] The distance between them is: {dis} kilometers\n", Colors.green, interval=0.1)
except Exception as e:
    # Handle any unexpected errors that may occur during execution
    Write.Print(f"[!] Error occurred: {e}\n", Colors.red, interval=0.1)
# Hold the program open until the user presses a key to exit
input("\n press any key to exit...")

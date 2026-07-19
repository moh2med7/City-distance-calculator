from pystyle import *
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from deep_translator import GoogleTranslator
import socket
import math
import folium
from folium.plugins import AntPath
import webbrowser
import os

# Initialize the geolocator with a user agent and timeout for requests
geolocator = Nominatim(user_agent="city_distance_calculator" , timeout=10)

# Set the translation flag to False by default.
USE_TRANSLATION = False

# Display the program title and description
print(Box.Lines("[+] Distance Calculator [+]"))
Write.Print("[-] this program for distance between cities \n" , Colors.blue_to_cyan , interval=0.05)

# define a function to check for internet connectivity  
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=1.0)
        return True
    except OSError:
        return False

def draw_map(lat1, lon1, lat2, lon2, city1_name, city2_name, bearing_deg):
    map_center = [(lat1 + lat2) / 2, (lon1 + lon2) / 2]
    my_map = folium.Map(location=map_center, zoom_start=4, tiles="OpenStreetMap")

    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    
    folium.Marker(
    location=point1,
    popup=f"Start: {city1_name}\n {point1}\nBearing to end: {bearing_deg:.2f}°",
    icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(my_map)
    
    folium.Marker(
    location=point2,
    popup=f"End: {city2_name}\n {point2}",
    icon=folium.Icon(color="green", icon="star")
    ).add_to(my_map)

    AntPath(
        locations=[point1, point2],
        color="blue",
        pulse_color="white",
        weight=4,
        opacity=0.8,
        delay=1000
    ).add_to(my_map)

    file_path = "navigation_map.html"
    my_map.save(file_path)

    print(f"[+] Map saved to: {file_path}")
    print("[+] Opening map in your web browser...")
    webbrowser.open('file://' + os.path.realpath(file_path))



# define a function to calculate the bearing between two geographic coordinates
def get_bearing(lat1, lon1, lat2, lon2):
    # transform the latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # calculate the difference in longitude to determine the direction if it is east (positive) or west (negative)
    d_lon = lon2 - lon1
    # calculate the bearing using the formula for initial bearing
    y = math.sin(d_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
    # calculate the initial bearing in radians and convert it to degrees
    bearing = math.atan2(y, x)
    bearing = (math.degrees(bearing) + 360) % 360
    
    # convert the bearing to a compass direction (N, NE, E, SE, S, SW, W, NW)
    directions = [
    "North",
    "North-East",
    "East",
    "South-East",
    "South",
    "South-West",
    "West",
    "North-West",
]
    idx = int((bearing + 22.5) / 45) % 8
    
    # return both the bearing in degrees and the corresponding compass direction
    return bearing, directions[idx]

# Check internet connection and ask for translation choice before entering the main loop
if check_internet():
            Write.Print("[+] Internet connection is active.\n", Colors.green, interval=0.1)
            print('\n')
            Write.Print("[?] Do you want to enable automatic translation for city names?", Colors.yellow, interval=0.05)
            print('\n')
            print("     1. Yes, enable automatic translation (recommended for non-English names)")
            print("     2. No, (write directly in English)")
            trans_choice = input("\nEnter choice number (1-2): ").strip()
            if trans_choice == '1':
                USE_TRANSLATION = True
                print("     [+] Translation enabled!")
            else:
                print("     [i] Translation disabled.")

# Main program loop
while True:
    try:
        # if there is no internet connection, prompt the user to check their network and retry
        if not check_internet():
            Write.Print("[!] No internet connection. Please check your network and try again.\n", Colors.red, interval=0.1)
            input("\n Press Enter to retry connection...")
            continue
        # Get city names from the user
        print()
        city1_input = input("Enter the first city name: ").strip()
        city2_input = input("Enter the second city name: ").strip()
        # check if either of the city names is empty
        if not city1_input or not city2_input:
            Write.Print('[-] City names cannot be empty. Try again.\n', Colors.red, interval=0.1)
            continue
        # translate the input if translation is enable
        if USE_TRANSLATION:
            try:
                city1_name = GoogleTranslator(source='auto', target='en').translate(city1_input)
                city2_name = GoogleTranslator(source='auto', target='en').translate(city2_input)
                print()
                print(f"[i] Translated: '{city1_input}' -> '{city1_name}'")
                print(f"[i] Translated: '{city2_input}' -> '{city2_name}'")
            # If translation fails, fallback to the original user input
            except Exception:
                city1_name = city1_input
                city2_name = city2_input
        # If translation is disabled, use original input directly
        else:
            city1_name = city1_input
            city2_name = city2_input
        # Fetch location details and coordinates for both cities
        location1 = geolocator.geocode(city1_name , language="en", exactly_one=True)
        location2 = geolocator.geocode(city2_name , language="en", exactly_one=True)
        # check if either of the locations is None (not found)
        if location1 is None or location2 is None:
            Write.Print("[-] One or both cities not found. Please check the names and try again.\n", Colors.red, interval=0.1)
            continue
        # check if both cities are the same
        elif (location1.latitude, location1.longitude) == (location2.latitude, location2.longitude):
            Write.Print("[-] Both cities are the same. Please enter different cities.\n", Colors.red, interval=0.1)
            continue
        # if both locations are valid and different, store the coordinates of both locations as (latitude, longitude) tuples
        f_p = (location1.latitude, location1.longitude)
        s_p = (location2.latitude, location2.longitude)
        # choose unit of measurement for distance calculation
        print('\n')
        Write.Print("[?] Choose unit of measurement for distance calculation:" , Colors.yellow , interval=0.05)
        print('\n')
        print("     1. Kilometers (km)")
        print("     2. Miles (mi)")
        unit_choice = input("\nEnter your Choice (1 or 2): ").strip()
        # Calculate the distance in the chosen unit of measurement
        if unit_choice == "2":
            dis = int(geodesic(f_p, s_p).miles)  # calculate in Miles
            unit_str = "miles"
            print('The unit of measurement will be in miles')
        elif unit_choice == '1':
            dis = int(geodesic(f_p, s_p).km) # calculate in Kilometers
            unit_str = 'kilometers'
            print('The unit of measurement will be in Kilometers')
        else:
            dis = int(geodesic(f_p, s_p).km)  # calculate in Kilometers
            unit_str = "kilometers"
            print('[!] Invalid choice. The unit of measurement will be in kilometers by default')
        # Extract the city names from the full address for display
        name1 = location1.address.split(',')[0].strip()
        country1 = location1.address.split(',')[-1].strip()
        name2 = location2.address.split(',')[0].strip()
        country2 = location2.address.split(',')[-1].strip()
        # Prepare display text for both cities, avoiding country name duplication
        display_text1 = name1 if name1 == country1 else f"{name1} ({country1})"
        display_text2 = name2 if name2 == country2 else f"{name2} ({country2})"
        # Display the visual destination box with the city names
        print()
        print()
        print(Box.DoubleCube(f"From: {display_text1}  to  {display_text2}  "))
        # Round the coordinates to 4 decimal places for better readability
        lat1, lon1 = round(location1.latitude, 4), round(location1.longitude, 4)
        lat2, lon2 = round(location2.latitude, 4), round(location2.longitude, 4)
        # Print coordinates of both cities side-by-side with their names
        Write.Print(f'\n[i] Coordinates:\n', Colors.yellow_to_red, interval=0.1)
        print(f"\t └──» {display_text1} ────────► ({lat1}, {lon1})")
        print(f"\t └──» {display_text2} ────────► ({lat2}, {lon2})")
        print()
        # Print the final calculated distance between the two cities in the chosen unit
        Write.Print(f"[-] The distance between them is: {dis} {unit_str}\n", Colors.green, interval=0.1)
        # print the bearing in degrees and compass direction
        bearing_deg, compass_dir = get_bearing(lat1, lon1, lat2, lon2)
        Write.Print(f"[i] Initial Bearing: {bearing_deg:.2f}° ({compass_dir})" , Colors.green , interval=0.1)
        print('\n')
        Write.Print("[?] Do you want to display the 2D Navigation Map?" , Colors.yellow , interval=0.05)
        print('\n')
        print('     1. Yes, show me the map')
        print('     2. No, skip the map')
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice == '1':
            draw_map(lat1, lon1, lat2, lon2, city1_name, city2_name, bearing_deg)
        elif choice == '2':
            print("[i] Skipping map display.")
        else:
            print("[!] Invalid choice. Skipping map display by default.")
        break
    # Handle any unexpected errors that may occur during execution
    except Exception as e:
        Write.Print(f"[!] Error occurred: {e}\n", Colors.red, interval=0.1)
# Hold the program open until the user presses a key to exit
input("\n press any key to exit...")

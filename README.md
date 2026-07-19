# 🗺️ Advanced Distance & Navigation Calculator

An interactive Python command-line tool designed to calculate precise geographic distances and bearings between cities worldwide using real-time coordinates. It also generates a 2D interactive map that opens automatically in your web browser.

## ✨ Key Features

- **Auto Internet Check**: Automatically verifies your network connection before running to prevent errors while fetching location data.
- **Smart City Geocoding**: Utilizes the Geopy library to fetch exact coordinates (latitude and longitude) and country names for any city input.
- **Measurement Options**: Allows users to calculate the distance in either Kilometers (km) or Miles (mi).
- **Initial Bearing & Compass Direction**: Calculates the exact initial navigation angle between two points and translates it into a compass direction (e.g., North-East).
- **Interactive 2D Map**: Generates a dynamic map using Folium, drawing a visual flight path (PolyLine) between both locations with informative custom markers.
- **Stylish CLI Visuals**: Features a clean, colorful, and animated terminal interface using pystyle and colorama.

## 🛠️ Dependencies & Installation

Make sure you have Python installed, then install the required external libraries using pip. Run the following command in your terminal:

```bash
pip install pystyle colorama geopy folium
```

**Libraries Used:**

- `geopy`: For geocoding addresses and calculating accurate geodesic distances.
- `folium`: For generating and rendering interactive HTML maps.
- `pystyle` & `colorama`: For adding color gradients and typewriter text effects to the console.
- `socket`, `math`, `webbrowser`, `os`: Built-in Python standard libraries for network checks, trigonometry, and file handling.

## 🚀 How to Run

1. Launch the script from your terminal or command prompt:
   ```bash
   python main.py
   ```
2. Enter the name of the first city, followed by the second city (supports multiple languages).
3. Select your preferred unit of measurement: `1` for Kilometers or `2` for Miles.
4. The program will display the precise coordinates, total distance, and initial bearing.
5. When prompted to display the 2D Navigation Map, type `1`. The program will save the map as `navigation_map.html` and launch it automatically in your default web browser.

## 📸 Generated Map Features

When you opt to generate the map, you will get a standalone HTML file containing:

- A **Red Marker** representing the starting city, displaying coordinates and the bearing angle when clicked.
- A **Green Star Marker** representing the destination city.
- A **Blue Path Line** showing the direct line-of-sight navigation route between both points.

> **Note:** This tool utilizes the OpenStreetMap service via Nominatim. An active internet connection is required to fetch city data accurately.
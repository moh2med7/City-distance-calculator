# 🗺️ Advanced Distance & Navigation Calculator

An interactive **Python** command-line tool designed to calculate precise geographic distances and bearings between cities worldwide using real-time coordinates. It also generates a 2D interactive map that opens automatically in your web browser.

---

## ✨ Key Features

* **Auto Internet Check:** Automatically verifies your network connection before running to prevent errors while fetching location data.
* **Smart City Geocoding:** Utilizes the `Geopy` library to fetch exact coordinates (latitude and longitude) and country names for any city input.
* **Measurement Options:** Allows users to calculate the distance in either Kilometers (`km`) or Miles (`mi`).
* **Initial Bearing & Compass Direction:** Calculates the exact initial navigation angle between two points and translates it into a compass direction (e.g., North-East).
* **Interactive 2D Map:** Generates a dynamic map using `Folium`, drawing a visual flight path (PolyLine) between both locations with informative custom markers.
* **Stylish CLI Visuals:** Features a clean, colorful, and animated terminal interface using `pystyle` and `colorama`.

---

## 🛠️ Dependencies & Installation

Make sure you have Python installed, then install the required external libraries using `pip`. Run the following command in your terminal:

```bash
pip install pystyle colorama geopy folium

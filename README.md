# 🗺️ City Distance Calculator

A simple Python CLI tool that calculates the distance and bearing between two cities. Type in any two city names and it'll geocode them, show you the distance (km or miles), the compass direction from one to the other, and optionally open an interactive map showing the route.

## ✨ Features

- Checks your internet connection before trying to fetch anything
- Can auto-translate city names to English if you type them in another language (uses Google Translate under the hood)
- Geocodes cities using Nominatim/OpenStreetMap via geopy
- Distance in km or miles, your choice
- Initial bearing + compass direction (like "North-East") between the two points
- Generates a 2D map (Folium) with markers and a path line, opens in your browser
- Colored terminal output via pystyle

## 🛠️ Setup

```
pip install -r requirements.txt
```

That installs everything (pystyle, geopy, folium, deep-translator) with the current tested versions, pinned in `requirements.txt`. Only the standard library stuff (socket, math, webbrowser, os) isn't in there since it comes with Python.

## 🚀 Usage

```
python distance-between-cities.py
```

When you run it:

1. It checks you're online
2. Asks if you want translation on (say yes if you're typing city names in Arabic, French, etc. — say no if you're just typing in English)
3. Enter city #1, then city #2
4. Pick km or miles
5. You get the coordinates, distance, and bearing printed out
6. Choose whether to open the map — if yes, it saves `navigation_map.html` and opens it automatically

## 📍 About the map

- Red marker = starting city (click it to see the bearing too)
- Green star marker = destination
- Blue line = the path between them

Needs an internet connection since it's pulling from OpenStreetMap/Nominatim.

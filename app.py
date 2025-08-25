import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import pandas as pd

# Sample data: City names and coordinates (longitude, latitude)
data = {
    "City": ["New York", "Los Angeles", "Chicago"],
    "Latitude": [40.7128, 34.0522, 41.8781],
    "Longitude": [-74.0060, -118.2437, -87.6298],
}

# Create geometry column from coordinates
geometry = [Point(xy) for xy in zip(data["Longitude"], data["Latitude"])]

# Create GeoDataFrame
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Set Coordinate Reference System (CRS) to WGS84 (EPSG:4326)
gdf.set_crs(epsg=4326, inplace=True)

# Pring the GeoDataFrame
print(gdf)

# Plot it
gdf.plot(marker="o", color="red", markersize=50)
plt.title("City Locations")
plt.show()
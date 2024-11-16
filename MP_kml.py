import pandas as pd
import simplekml
import requests
import ipaddress

# Load the network data
df = pd.read_csv('network_data.csv')

# Create a KML object
kml = simplekml.Kml()

# Function to get coordinates from IP using ipinfo.io API
def get_coords_from_ip(ip, token):
    # Check if the IP is in the specified range
    if ipaddress.ip_address(ip) in ipaddress.ip_network('192.168.0.0/16'):
        return (78.000828,30.266739) #Home Location
    if ipaddress.ip_address(ip) in ipaddress.ip_network('224.0.0.0/8'):
        return (-0.119386,51.522961) #London Location
    # Use ipinfo.io API for other IPs
    url = f"https://ipinfo.io/{ip}/json?token={token}"
    response = requests.get(url)
    data = response.json()
    if 'loc' in data:
        lat, lon = map(float, data['loc'].split(','))
        return (lon, lat)  # KML uses (longitude, latitude)
    else:
        print(f"No coordinates found for IP: {ip}")
        return None

# Your ipinfo.io API token
api_token = 'b74df0a876f005'

# Dictionary to store coordinates for each IP
ip_coords = {}

# Add lines between source and destination IPs
for index, row in df.iterrows():
    src_ip = row['Source IP']
    dst_ip = row['Destination IP']

    # Get coordinates for source IP
    if src_ip not in ip_coords:
        src_coords = get_coords_from_ip(src_ip, api_token)
        if src_coords:
            ip_coords[src_ip] = src_coords
        else:
            continue  # Skip if no coordinates found
    src_coords = ip_coords[src_ip]

    # Get coordinates for destination IP
    if dst_ip not in ip_coords:
        dst_coords = get_coords_from_ip(dst_ip, api_token)
        if dst_coords:
            ip_coords[dst_ip] = dst_coords
        else:
            continue  # Skip if no coordinates found
    dst_coords = ip_coords[dst_ip]

    # Add line to KML
    line = kml.newlinestring(name=f"Packet {index+1}",
                             description=f"Source: {src_ip}\nDestination: {dst_ip}\nProtocol: {row['Protocol']}\nLength: {row['Length']}",
                             coords=[src_coords, dst_coords])
    line.style.linestyle.color = simplekml.Color.red
    line.style.linestyle.width = 2

# Save to KML file
kml.save('network_lines.kml')

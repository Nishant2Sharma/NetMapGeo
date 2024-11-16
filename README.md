# NetMapGeo

**NetMapGeo** is a network visualization tool designed to capture, analyze, and visualize network traffic flows. The project integrates Wireshark for packet capture, processes the raw data into a structured CSV format, and then generates KML files for visualizing network communications on mapping platforms like Google Earth or My Maps. This project is useful for network analysis, monitoring, and educational purposes.

## Key Features

- **Packet Capture**: Uses **Wireshark** to capture network packets for analysis, offering a detailed view of network traffic.
- **Data Processing**: Converts packet data into **CSV** format for easy handling and analysis.
- **Visualization**: Generates **KML files** for use in platforms like **Google Earth** or **My Maps**, enabling users to visualize the network traffic patterns in 2D/3D maps.
- **Customizable**: Filter and analyze data by **source/destination IPs**, **protocols**, and **ports**.
- **Educational and Analytical Tool**: Ideal for network engineers, cybersecurity professionals, and educators looking to gain insights into network behavior or teach networking concepts.

## Usage

### Prerequisites

Before using NetMapGeo, ensure you have the following software installed:
- **Wireshark**: For capturing network packets.
- **Python**: Required for running the processing and KML generation scripts.

### Capturing Network Packets

- Open **Wireshark** and select the network interface (e.g., Wi-Fi, Ethernet) you want to capture traffic on.
- Start capturing network traffic.
- Save the captured packets as a **.pcap** file.

### Run Plotting Script

- To plot the network data, run the **plot.py** script.
- The script will read the **network_data.csv** file.
- It will then generate a bar plot that shows the number of packets for each protocol found in the dataset (e.g., TCP, UDP, ICMP).

### Processing Captured Data

- Run the Python script **MP_csv.py** to convert the .pcap file into a CSV format.
- This will generate a CSV file containing the captured packet data, including details like source/destination IPs, protocols, ports, and packet sizes.

### Generating KML for Visualization

- Run the Python script **MP_kml.py** to convert the CSV file into a KML file.
- The output will be a KML file that can be opened in mapping tools like Google Earth or My Maps to visualize network traffic flows.

## Technologies Used

- **Wireshark**: A widely-used network protocol analyzer for capturing and inspecting network packets. It is the primary tool for packet capture in this project.
- **Python**: The programming language used for processing the captured network data and generating the KML files for visualization. Python provides a flexible and powerful environment for data manipulation and analysis.
- **pandas**: A Python library used for data manipulation and analysis, especially for handling and processing CSV files generated from packet captures.
- **Matplotlib**: A powerful Python library for creating static, interactive, and animated visualizations. It is used for visualizing network traffic data before converting it into KML format.
- **SimpleKML**: A Python library used to generate KML (Keyhole Markup Language) files, which are used for visualizing geographic data in tools like Google Earth or My Maps.
- **Scapy**: A packet manipulation tool that allows for the creation, manipulation, and analysis of network packets. It is used for more advanced packet analysis and can work with Wireshark captures.
- **Requests**: A simple, yet powerful HTTP library for making API calls. It is used to interact with external APIs or web services if needed during the data processing phase.
- **ipinfo.io**: A service for IP geolocation and information lookup. It provides details like geographical location, organization, and other metadata associated with an IP address, which can be used for mapping or traffic analysis.
- **Google Earth/My Maps**: Platforms for visualizing KML files. These tools allow users to visualize network traffic flows geographically, aiding in the analysis of communication patterns between source and destination IPs.

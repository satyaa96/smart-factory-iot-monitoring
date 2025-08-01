# 🏭 Smart Factory IoT Monitoring System

This project demonstrates a complete end-to-end **IoT monitoring system** using **AWS IoT Core**, **DynamoDB**, **Amazon S3**, and **Power BI**. It simulates sensor data from factory devices, stores the data in the cloud, and visualizes it for analysis.

---

## 🔧 Technologies Used

- **Python** – Device simulation and data formatting
- **AWS IoT Core** – MQTT messaging and rule engine
- **AWS DynamoDB** – Real-time sensor data storage
- **Amazon S3** – Log backup in JSON format
- **Power BI Web** – Dashboard visualization
- **Git & GitHub** – Version control and project sharing

---

## ✅ Skills Demonstrated

- **IoT Development:** Simulated real-time sensor data using MQTT protocol and AWS IoT Core.
- **Cloud Architecture:** Integrated cloud services (DynamoDB and S3) for scalable data storage.
- **Automation with Python:** Automated data simulation and format conversion (JSON → CSV).
- **Data Visualization:** Built a Power BI dashboard for real-time monitoring and analysis.
- **End-to-End System Integration:** Connected edge-to-cloud pipeline from device to dashboard.
- **Version Control:** Managed and documented code via GitHub.
- **Smart Factory / DX Readiness:** Project mirrors real-world smart manufacturing use cases.

---

## 📁 Project Structure

```bash
smart-factory-iot-monitoring/
├── simulate_sensor.py        # Publishes simulated sensor data to AWS IoT
├── factory_data.json         # Sample IoT message log (from S3)
├── factory_data.csv          # Converted data for Power BI
├── convert_json_to_csv.py    # Script to convert JSON to CSV
└── README.md                 # Project documentation

🚀 How It Works
✅ Step 1: Simulate Data
Run the simulator script:
python3 simulate_sensor.py
Publishes MQTT data to topic:
factory/FactorySensor1/data

✅ Step 2: AWS IoT Rules
Rule 1: Store real-time data in DynamoDB → FactorySensorData
Rule 2: Archive all messages to Amazon S3 as factory_data.json

✅ Step 3: Convert JSON to CSV
Run:
python3 convert_json_to_csv.py

✅ Step 4: Power BI Visualization
Go to Power BI Web
Click Create → Paste or Upload your data
Upload factory_data.csv

Then create:
📈 Line chart: Temperature vs Time
📊 Bar chart: Humidity by Device
📋 Table: Raw data



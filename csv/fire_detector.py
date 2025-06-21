"""
1,2,3 sensors

windows of 5 seconds

read csv

tuple 3 values
#sort by timestamp

t,alert
1,
1,
2
3
4
5
6
7
8

initial_time = 0
dict = defaultdict(list)
if current_time - initial_time <=  5:
    dict[sensor_id].append(smoke_level)
else:
   for sensor_id, smoke_level in dict.items():
        avg 
        if avg > 10



1,0.2834890812835171,1715698800
2,3.6591534314666987,1715698800
3,3.037402281028486,1715698800
1,6.990739288554613,1715698801
2,7.798725440530098,1715698801
3,3.095143519415115,1715698801
1,9.711615229054582,1715698802
"""

import csv
from collections import defaultdict
import pandas as pd


def fire_detector(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        prev_time = None
        sensor_smoke_level = defaultdict(list)
        header = next(reader)
        for row in reader:
            sensor_id = int(row[0])
            smoke_level = float(row[1])
            current_time = int(row[2])
            if prev_time and current_time - prev_time <= 5:
                print(f"Creating window: prev_time: {prev_time}, current_time: {current_time}")
                sensor_smoke_level[sensor_id].append(smoke_level)
            else:
                print(f"reset new window: current_time: {current_time}")
                #read the map
                print(sensor_smoke_level)
                sensor_smoke_level = defaultdict(list)
            prev_time = current_time


def fire_detection_system(file_path):
    df = pd.read_csv(file_path, nrows=100)
    #print(df)
    df_sorted = df.sort_values(by='Timestamp')
    #print(df_sorted)
    prev_time = None
    sensor_smoke_level = defaultdict(list)
    sensor_ids = df['Sensor ID'].unique()
    alert_state = {sid: False for sid in sensor_ids}
    all_alert = False
    for _,row in df_sorted.iterrows():
        sensor_id = row["Sensor ID"]
        smoke_level = row["Smoke Level (ppm)"]
        current_time = row["Timestamp"]
        window = df[
            (df['Sensor ID'] == sensor_id) &
            (df['Timestamp'] >= current_time - 5) &
            (df['Timestamp'] <= current_time)
        ]
        #print(window)
        avg = window['Smoke Level (ppm)'].mean()
        alert_state[sensor_id] = avg > 10.0

        # Check if all sensors are in alert
        if all(alert_state.values()) and not all_alert:
            print(f"Timestamp: {current_time} - ALL SENSORS IN ALERT")
            all_alert = True
        # Reset alert when all sensors are out of alert
        if not any(alert_state.values()) and all_alert:
            print(f"Timestamp: {current_time} - ALL CLEAR")
            all_alert = False
        """
        #print(row)
        if prev_time and current_time - prev_time <= 5:
            print(f"Creating window: prev_time: {prev_time}, current_time: {current_time}")
            sensor_smoke_level[sensor_id].append(smoke_level)
        else:
            print(f"reset new window: current_time: {current_time}")
            #read the map
            print(sensor_smoke_level)
            sensor_smoke_level = defaultdict(list)
        prev_time = current_time
        """
    """
    # Load the CSV file into a DataFrame
    #Sensor ID,Smoke Level (ppm),Timestamp
    # Convert the UNIX Timestamp to datetime for easier processing
    data["Timestamp"] = pd.to_datetime(data["Timestamp"], unit='s')
    
    # Sort the data by timestamp
    data = data.sort_values(by="Timestamp")
    
    # Initialize variables to track alert status
    sensor_alert_status = {}
    all_sensors_in_alert = False
    
    # Process the data row by row
    for index, row in data.iterrows():
        sensor_id = row["Sensor ID"]
        smoke_level = row["Smoke Level"]
        timestamp = row["Timestamp"]
        
        # Filter data for the past 5 seconds for the current sensor
        past_5_seconds_data = data[
            (data["Sensor ID"] == sensor_id) &
            (data["Timestamp"] >= timestamp - pd.Timedelta(seconds=5)) &
            (data["Timestamp"] <= timestamp)
        ]
        
        # Calculate the average smoke level over the past 5 seconds
        avg_smoke_level = past_5_seconds_data["Smoke Level"].mean()
        
        # Update the sensor's alert status
        sensor_alert_status[sensor_id] = avg_smoke_level > 10.0
        
        # Check if all sensors are in alert
        if all(sensor_alert_status.values()) and not all_sensors_in_alert:
            print(f"Timestamp: {timestamp} - ALL SENSORS IN ALERT")
            all_sensors_in_alert = True
        
        # Check if all sensors have dropped out of alert
        if not any(sensor_alert_status.values()) and all_sensors_in_alert:
            print(f"Timestamp: {timestamp} - ALL CLEAR")
            all_sensors_in_alert = False
    """

def fire_detection_system2(file_path):
    df = pd.read_csv(file_path, nrows=100)
    #print(df)
    df_sorted = df.sort_values(by='Timestamp')
    #print(df_sorted)
    prev_time = None
    sensor_smoke_level = defaultdict(list)
    sensor_ids = df['Sensor ID'].unique()
    alert_state = {sid: False for sid in sensor_ids}
    all_alert = False
    for index,row in enumerate(df_sorted.iterrows()):
        print(f"index: {index}, row: {row}")
        sensor_id = row["Sensor ID"]
        smoke_level = row["Smoke Level (ppm)"]
        current_time = row["Timestamp"]
        #if 

#fire_detector('smoke_sensor_data.csv')
fire_detection_system2('smoke_sensor_data.csv')
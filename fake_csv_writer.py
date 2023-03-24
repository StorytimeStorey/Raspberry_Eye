import csv
import random

# # Open a CSV file for writing
# with open('fake_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     # Write the header row
#     writer.writerow(['Time', 'Temperature', 'Humidity', 'Heater on', 'Cooler on', 'Humidifier on', 'Alerts'])

#     # Generate 24 hours of fake data
#     for hour in range(24):
#         for minute in range(0, 60, 5):
#             time = f"{hour:02}{minute:02}"
#             temperature = round(random.uniform(20, 30), 1)
#             humidity = round(random.uniform(40, 60), 1)
#             heater_on = random.randint(0, 1)
#             cooler_on = random.randint(0, 1)
#             humidifier_on = random.randint(0, 1)
#             alerts = random.randint(0, 1)

#             # Write the data row
#             writer.writerow([time, temperature, humidity, heater_on, cooler_on, humidifier_on, alerts])


import csv
import matplotlib.pyplot as plt

# Read the data from the CSV file
def make_graph():

    with open('fake_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Extract the temperature and humidity data
    times = [row['Time'] for row in data]
    temperatures = [float(row['Temperature']) for row in data]
    humidities = [float(row['Humidity']) for row in data]

    # Create the plot
    plt.plot(times, temperatures, label='Temperature')
    plt.plot(times, humidities, label='Humidity')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Temperature and Humidity Over Time')
    plt.legend()
    plt.savefig('temperature_and_humidity.png', dpi=300)

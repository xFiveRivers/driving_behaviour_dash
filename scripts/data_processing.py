import pandas as pd
import os
import glob

# Get raw file names
raw_files = glob.glob('../data/raw/*.csv')

# Path to save the processed files
processed_path = '../data/processed/'


# Loop over raw files, add column names, save to new directory
for count, file in enumerate(raw_files):
    df = pd.read_csv(file,
                        names = ['Time (s)', 'Speed (m/s)', 'Gear', 'Engine Load (% of Max Power)', 'Total Acc (m/s^2)', 
                                'Engine RPM', 'Pitch (deg)', 'Lateral Acc (m/s^2)', 'Passenger Count', 'Load Ind', 
                                'AC Level', 'Window Opening', 'Radio Volume', 'Rain Intensity', 'Visibility', 
                                'Driver Wellbeing', 'Driver Rush'],
                        )
    df = df.set_index('Time (s)')
    file_name = f'Trip_{count+1}'
    df.to_csv(processed_path+file_name)
from remote_scope import *
import pandas as pd
import datetime
import os

scopeChannels = {'INT01_DRIVER': '2', 'INT01': '3'}
runNumber = 1

# All possible options for scope columns
scope_columns = {'runNumber': {'name': 'Run Number', 'type': 'scalar'},
                 'tUnit': {'name': 'Time Unit', 'type': 'scalar'},
                 'time': {'name': 'Time', 'type': 'array'},
                 'INT01': {'name': 'INT01 (V)', 'type': 'array'},
                 'INT02': {'name': 'INT02 (V)', 'type': 'array'},
                 'INT01_DRIVER': {'name': 'INT01 Driver (V)', 'type': 'array'},
                 'INT02_DRIVER': {'name': 'INT02 Driver (V)', 'type': 'array'},
                 'ACC01': {'name': 'ACC01 (V)', 'type': 'array'},
                 'ACC02': {'name': 'ACC02 (V)', 'type': 'array'}}

saveFolder = '/'

# Connect to the scope
try:
    scope = Oscilloscope(scopeChannels)
except pyvisa.errors.VisaIOError:
    print('Could not connect to the scope')

scope.read_scope()


# Save scope results'
scope_filename = f'CMFX_{runNumber}_scope.csv'
scope.set_runNumber(runNumber)

# Date
now = datetime.datetime.now()
runDate = now.date().strftime('%Y_%m_%d')
# Create a folder for today's date if it doesn't already exist
if runDate not in os.listdir(saveFolder):
    os.mkdir(f'{saveFolder}/{runDate}')

# These results are listed in accordance with the 'columns' variable in constants.py
# If the user would like to add or remove fields please make those changes in constant.py
results = [getattr(scope, variable) for variable in scope_columns if hasattr(scope, variable)]

# Creates a data frame which is easier to save to csv formats
results_df = pd.concat([pd.Series(val) for val in results], axis=1)
results_df.columns = [scope_columns[variable]['name'] for variable in scope_columns if hasattr(scope, variable)]
results_df.to_csv(f'{saveFolder}/{runDate}/{scope_filename}', index=False)
print('Done saving scope!')
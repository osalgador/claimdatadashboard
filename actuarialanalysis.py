import pandas as pd
import numpy as np
#i11mportramos nuestros datos como dataframes
dfcarIns= pd.read_csv("Insurance claims data.csv")#DATAFRAME VEHICLE RISK ANALYSIS
dfLife=pd.read_csv("Insurance_claims.csv")#DATAFRAME LIFE & FRAUD ANALYSIS
dfcarIns.shape
dfcarIns.info()
dfcarIns.head()
#Elimanremos datos vacíos y datos que no aporten al modelo
dfcarIns.isnull().sum()
dfcarIns=dfcarIns.drop(columns=["policy_id"])
#mapearemos toda columna que tenga datos de si y no para volverlos binarios y usarlos en nuestro análisis
dftobinary=dfcarIns[['is_esc',#Se creará un dataframe con las columnas que se harán binarias 
'is_adjustable_steering',
'is_tpms',
'is_parking_sensors',
'is_parking_camera',
'is_front_fog_lights',
'is_rear_window_wiper',
'is_rear_window_washer',
'is_rear_window_defogger',
'is_brake_assist',
'is_power_door_locks',
'is_central_locking',
'is_power_steering',
'is_driver_seat_height_adjustable',
'is_day_night_rear_view_mirror',
'is_ecw',
'is_speed_alert']]
print(dftobinary)
binary_columns = [
'is_esc',
'is_adjustable_steering',
'is_tpms',
'is_parking_sensors',
'is_parking_camera',
'is_front_fog_lights',
'is_rear_window_wiper',
'is_rear_window_washer',
'is_rear_window_defogger',
'is_brake_assist',
'is_power_door_locks',
'is_central_locking',
'is_power_steering',
'is_driver_seat_height_adjustable',
'is_day_night_rear_view_mirror',
'is_ecw',
'is_speed_alert'
]

for col in binary_columns:
    dfcarIns[col] = dfcarIns[col].map({'Yes':1, 'No':0})
#Confirmamos que el dataframe ha sido cambiado completamente
#print(dftobinary)
#Cambiaremos el valor de "Max torque" y "Max power" para no descartar los datos usando unicamente los valores numéricos
dfcarIns['max_torque'] = dfcarIns['max_torque'].str.extract('(\d+)').astype(float)
dfcarIns['max_power'] = dfcarIns['max_power'].str.extract('(\d+)').astype(float)
print(dfcarIns[['max_power','max_torque']])
#Se creará nuevas variables para mejorar el modelo usado 
dfcarIns['power_weight_ratio'] = dfcarIns['max_power'] / dfcarIns['gross_weight']#con esta variable veremos que tan potente es el vehículo conforme a su peso
dfcarIns['young_driver'] = (dfcarIns['customer_age'] < 25).astype(int)#estadísticamente los jovenes menores de 25 tienden a tener más accidentes
#Estas dos variables permitirán analizar los conductores jóvenes y el número de los reclamos que existen entre ellos
dfcarIns.to_csv("insurance_dashboard_dataset.csv", index=False)
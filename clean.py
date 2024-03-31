import pandas as pd

file_path = r"C:\Users\haoha\OneDrive\Desktop\personal\Personal Projects\SG Toilet Ratings\SG Toilet Ratings Updated.xlsx"
general_data = pd.read_excel(file_path, sheet_name="General Data")

print(general_data.head())

general_data.columns = ['Type', 'Location', 'TotalScore', 'CleanlinessScore', 'ScentScore', 'AestheticsScore', 'MusicScore', 'ToiletPaper', 'HandTowel', 'HandDryer', 'HandSoap', 'SeatCleaner', 'MirrorMaintenance', 'TapMaintenance', 'UrinalMaintenance', 'ToiletMaintenance', 'DoorLock', 'CoatHook', 'Bidet', 'AutoFlush', 'AutoTap', 'AutoSoap', 'BinNotFull', 'FeedbackAvailable', 'AmbulantFacilities', 'ChildFacilities', 'Signages', 'Posters', 'OtherRemarks']

print(general_data.head())

general_data.to_excel('Cleaned_SG_Toilet_Ratings.xlsx', index=False)



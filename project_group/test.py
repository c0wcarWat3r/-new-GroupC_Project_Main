from pathlib import Path 
file_path = Path.cwd()/"project_group"/"csv_reports"/"cash-on-hand-usd-42.csv"
print(file_path.exists())
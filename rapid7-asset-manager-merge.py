#!/usr/bin/env python
import pandas as pd

# Asset Management tool's generated csv of all assets
asset_mgr_url = "https://assetmanager/server_combo.csv"
# Rapid7's exported csv showing all assets affected by a given vuln
vulnlist = "CVE-2019-11477.csv"
# Name of the new csv that combines the two above
csv_file = "new.csv"
# Choose what headers I want to see in my new csv
header = ['Asset','Name_y','Proof', 'Lifecycle', 'Platform', 'Purpose', 'Contact']

# Creating a Pandas Dataframe from the combo list
rundeck_df = pd.read_csv(asset_mgr_url, sep=',', index_col=False, header=0 )

# Creating a Pandas Dataframe from the combo list
vulnlist_df = pd.read_csv(vulnlist, sep=',', index_col=False, header=0 )

# Merge rundeck and vulnlist on their respective IP columns
merge_df = pd.merge(vulnlist_df, rundeck_df, left_on='Asset', right_on='Ip_address')

# Sort by Lifecycle for ease of patch rollouts
sorted_df = merge_df.sort_values(by="Lifecycle")

# create new csv
sorted_df.to_csv(csv_file, columns = header, index=False)


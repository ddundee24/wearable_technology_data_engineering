
import requests 
import pandas as pd
from dotenv import load_dotenv 
import os

load_dotenv()
token = os.getenv("token")
base_url = os.getenv("base_url")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}


def get_athlete_data():
    url=f"{base_url}athletes"
    response = requests.get(url,headers=headers)
    return pd.json_normalize(response.json())
def get_period_data():
    url=f"{base_url}periods"
    response = requests.get(url,headers=headers)
    return pd.json_normalize(response.json())
def get_activities_data():
    url=f"{base_url}activities"
    response = requests.get(url,headers=headers)
    return pd.json_normalize(response.json())


athlete_df = get_athlete_data()
period_df = get_period_data()
activity_df = get_activities_data()


### Athlete Detail
athlete_ids = athlete_df['id'].unique()
athlete_detail = []

for athlete_id in athlete_ids:
    url=f"{base_url}athletes/{athlete_id}"
    response = requests.get(url,headers=headers)
    ## Normalize and flatten if successful
    if response.status_code == 200:
        data = response.json()
        flat = pd.json_normalize(data)
        flat['athlete_id'] = athlete_id ## foreign key
        athlete_detail.append(flat)
    else:
        print(f"Failed for athlete {athlete_id}:{response.status_code}")
## Final athlete output
athlete_detail_df = pd.concat(athlete_detail,ignore_index=True)


### Periods Detail
period_ids = period_df['id'].unique()
period_detail = []

for period_id in period_ids:
    url=f"{base_url}periods/{period_id}"
    response = requests.get(url,headers=headers)
    ## Normalize and flatten if successful
    if response.status_code == 200:
        data = response.json()
        flat = pd.json_normalize(data)
        flat['period_id'] = period_id ## foreign key
        period_detail.append(flat)
    else:
        print(f"Failed for period {period_id}:{response.status_code}")
## Final period output
period_detail_df = pd.concat(period_detail,ignore_index=True)

### Periods Athletes Detail
period_athlete_ids = period_df['id'].unique()
period_athlete_detail = []

for period_athlete_id in period_athlete_ids:
    url=f"{base_url}periods/{period_id}/athletes"
    response = requests.get(url,headers=headers)
    ## Normalize and flatten if successful
    if response.status_code == 200:
        data = response.json()
        flat = pd.json_normalize(data)
        flat['period_id'] = period_id ## foreign key
        period_athlete_detail.append(flat)
    else:
        print(f"Failed for period {period_id}:{response.status_code}")
## Final period output
period_athlete_detail_df = pd.concat(period_athlete_detail,ignore_index=True)

## Activity Details
activity_ids = activity_df['id'].unique()
activity_detail = []

for activity_id in activity_ids:
    url=f"{base_url}activities/{activity_id}"
    response = requests.get(url,headers=headers)
    ## Normalize and flatten if successful
    if response.status_code == 200:
        data = response.json()
        flat = pd.json_normalize(data)
        flat['activity_id'] = activity_id ## foreign key
        activity_detail.append(flat)
    else:
        print(f"Failed for activity {activity_id}:{response.status_code}")
## Final period output
activity_detail_df = pd.concat(activity_detail,ignore_index=True)

### Activity Athletes Detail
activity_athlete_ids = activity_df['id'].unique()
activity_athlete_detail = []

for activity_athlete_id in activity_athlete_ids:
    url=f"{base_url}activities/{activity_athlete_id}/athletes"
    response = requests.get(url,headers=headers)
    ## Normalize and flatten if successful
    if response.status_code == 200:
        data = response.json()
        flat = pd.json_normalize(data)
        flat['activity_id'] = activity_id ## foreign key
        activity_athlete_detail.append(flat)
    else:
        print(f"Failed for activity {activity_id}:{response.status_code}")
## Final period output
activity_athlete_detail_df = pd.concat(activity_athlete_detail,ignore_index=True)

### Activity Periods Detail
activity_period_ids = activity_df['id'].unique()
activity_period_detail = []

for activity_period_id in activity_period_ids:
    url=f"{base_url}activities/{activity_period_id}/periods"
    response = requests.get(url,headers=headers)
    ## Normalize and flatten if successful
    if response.status_code == 200:
        data = response.json()
        flat = pd.json_normalize(data)
        flat['activity_period_id'] = activity_period_id ## foreign key
        activity_period_detail.append(flat)
    else:
        print(f"Failed for activity {activity_id}:{response.status_code}")
## Final period output
activity_period_detail_df = pd.concat(activity_period_detail,ignore_index=True)

print(athlete_detail_df.columns.tolist())
athlete_columns = ['athlete_id','first_name','last_name','height','weight','velocity_max','acceleration_max','max_player_load_per_minute','position_id','position_name','is_deleted']
athlete_final = athlete_detail_df[athlete_columns]
print(athlete_final.columns.tolist())
athlete_final.head()

print(period_detail_df.columns.tolist())
period_columns = ['period_id','activity_id','name','start_time','end_time','is_deleted']
period_final = period_detail_df[period_columns]
period_final.head()


print(period_athlete_detail_df.columns.to_list())
period_athlete_columns = ['id','period_id','first_name','last_name'] 
period_athlete_final = period_athlete_detail_df[period_athlete_columns]
period_athlete_final.rename(columns={'id':'athlete_id'},inplace=True)
period_athlete_final.head()

print(activity_period_detail_df.columns.tolist())
activity_period_columns = ['activity_id','period_depth_id','name','start_time','end_time']
activity_period_final = activity_period_detail_df[activity_period_columns]
activity_period_final.head()

print(activity_athlete_detail_df.columns.tolist())
activity_athlete_columns = ['activity_id','activity_athlete_id','first_name','last_name']
activity_athlete_final = activity_athlete_detail_df[activity_athlete_columns]
activity_athlete_final.head()
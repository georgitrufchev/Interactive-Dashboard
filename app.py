import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Afghanistan Natural Disaster Dashboard 2024')

DATA_URL = 'afghanistan-natural-disaster-incidents-from-january-to-december-2024.csv'

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL, skiprows=1)
    data.columns = ['Region', 'Prov_Code', 'Province', 'Dist_Code', 'District',
                    'Date', 'Disaster_Type', 'Persons_Killed', 'Persons_Injured',
                    'Families_Affected', 'Individuals_Affected', 'Houses_Damaged',
                    'Houses_Destroyed']
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data['date'] = pd.to_datetime(data['date'], dayfirst=True)
    data['month'] = data['date'].dt.month_name()
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Done! (using st.cache_data)')

st.header('Analysing Natural Disaster Incidents Across Afghanistan')
st.markdown('This dashboard presents key insights from the Afghanistan Natural Disaster Incidents dataset January to December 2024 sourced from the Humanitarian Data Exchange HDX.')

st.sidebar.title('Dashboard Filters')
st.sidebar.markdown('Use the filters below to explore the data.')

selected_disaster = st.sidebar.radio(
    'Select Disaster Type',
    ['All', 'Earthquake', 'Flood / flash flood', 'Landslide / mudflow', 'Heavy snowfall']
)

selected_region = st.sidebar.selectbox(
    'Select Region',
    ['All', 'Eastern', 'Northern', 'North Eastern', 'Southern',
     'South Eastern', 'Capital', 'Western', 'Central Highland']
)

if selected_disaster == 'All':
    filtered_data = data
if selected_disaster == 'Earthquake':
    filtered_data = data[data['disaster_type'] == 'Earthquake']
if selected_disaster == 'Flood / flash flood':
    filtered_data = data[data['disaster_type'] == 'Flood / flash flood']
if selected_disaster == 'Landslide / mudflow':
    filtered_data = data[data['disaster_type'] == 'Landslide / mudflow']
if selected_disaster == 'Heavy snowfall':
    filtered_data = data[data['disaster_type'] == 'Heavy snowfall']

if selected_region == 'Eastern':
    filtered_data = filtered_data[filtered_data['region'] == 'Eastern']
if selected_region == 'Northern':
    filtered_data = filtered_data[filtered_data['region'] == 'Northern']
if selected_region == 'North Eastern':
    filtered_data = filtered_data[filtered_data['region'] == 'North Eastern']
if selected_region == 'Southern':
    filtered_data = filtered_data[filtered_data['region'] == 'Southern']
if selected_region == 'South Eastern':
    filtered_data = filtered_data[filtered_data['region'] == 'South Eastern']
if selected_region == 'Capital':
    filtered_data = filtered_data[filtered_data['region'] == 'Capital']
if selected_region == 'Western':
    filtered_data = filtered_data[filtered_data['region'] == 'Western']
if selected_region == 'Central Highland':
    filtered_data = filtered_data[filtered_data['region'] == 'Central Highland']

st.markdown('---')

st.subheader('Key Statistics')
st.write('Total Incidents:', filtered_data.shape[0])
st.write('Total Deaths:', filtered_data['persons_killed'].sum())
st.write('Total Injured:', filtered_data['persons_injured'].sum())
st.write('Total Individuals Affected:', filtered_data['individuals_affected'].sum())
st.write('Total Families Affected:', filtered_data['families_affected'].sum())

st.markdown('---')

st.subheader('Number of Incidents by Disaster Type')
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(
    ['Earthquake', 'Flood / flash flood', 'Landslide / mudflow', 'Heavy snowfall'],
    [
        filtered_data[filtered_data['disaster_type'] == 'Earthquake'].shape[0],
        filtered_data[filtered_data['disaster_type'] == 'Flood / flash flood'].shape[0],
        filtered_data[filtered_data['disaster_type'] == 'Landslide / mudflow'].shape[0],
        filtered_data[filtered_data['disaster_type'] == 'Heavy snowfall'].shape[0]
    ],
    color='steelblue'
)
ax1.set_xlabel('Disaster Type')
ax1.set_ylabel('Number of Incidents')
ax1.set_title('Incidents by Disaster Type')
ax1.set_xticks(range(4))
ax1.set_xticklabels(['Earthquake', 'Flood / flash flood', 'Landslide / mudflow', 'Heavy snowfall'], rotation=45)
st.pyplot(fig1)

st.markdown('---')

st.subheader('Deaths by Region')
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(
    ['Eastern', 'Northern', 'North Eastern', 'Southern',
     'South Eastern', 'Capital', 'Western', 'Central Highland'],
    [
        filtered_data[filtered_data['region'] == 'Eastern']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'Northern']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'North Eastern']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'Southern']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'South Eastern']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'Capital']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'Western']['persons_killed'].sum(),
        filtered_data[filtered_data['region'] == 'Central Highland']['persons_killed'].sum()
    ],
    color='red'
)
ax2.set_xlabel('Region')
ax2.set_ylabel('Deaths')
ax2.set_title('Deaths by Region')
ax2.set_xticks(range(8))
ax2.set_xticklabels(['Eastern', 'Northern', 'North Eastern', 'Southern',
                     'South Eastern', 'Capital', 'Western', 'Central Highland'], rotation=45)
st.pyplot(fig2)

st.markdown('---')

st.subheader('Incidents by Month')
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_counts = [
    filtered_data[filtered_data['month'] == 'January'].shape[0],
    filtered_data[filtered_data['month'] == 'February'].shape[0],
    filtered_data[filtered_data['month'] == 'March'].shape[0],
    filtered_data[filtered_data['month'] == 'April'].shape[0],
    filtered_data[filtered_data['month'] == 'May'].shape[0],
    filtered_data[filtered_data['month'] == 'June'].shape[0],
    filtered_data[filtered_data['month'] == 'July'].shape[0],
    filtered_data[filtered_data['month'] == 'August'].shape[0],
    filtered_data[filtered_data['month'] == 'September'].shape[0],
    filtered_data[filtered_data['month'] == 'October'].shape[0],
    filtered_data[filtered_data['month'] == 'November'].shape[0],
    filtered_data[filtered_data['month'] == 'December'].shape[0]
]
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.plot(month_order, monthly_counts, marker='o', color='darkorange')
ax3.set_xlabel('Month')
ax3.set_ylabel('Number of Incidents')
ax3.set_title('Disaster Incidents by Month 2024')
ax3.set_xticks(range(12))
ax3.set_xticklabels(month_order, rotation=45)
st.pyplot(fig3)

st.markdown('---')

st.subheader('Families Affected by Province (Top 10)')
province_families = pd.DataFrame({
    'Families Affected': [
        filtered_data[filtered_data['province'] == 'Ghor']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Nangarhar']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Baghlan']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Kunar']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Faryab']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Badakhshan']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Badghis']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Laghman']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Farah']['families_affected'].sum(),
        filtered_data[filtered_data['province'] == 'Kabul']['families_affected'].sum()
    ]
}, index=['Ghor', 'Nangarhar', 'Baghlan', 'Kunar', 'Faryab',
          'Badakhshan', 'Badghis', 'Laghman', 'Farah', 'Kabul'])
st.area_chart(province_families)

st.markdown('---')

st.subheader('Houses Damaged vs Destroyed by Disaster Type')
x = np.arange(4)
fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.bar(x - 0.2, [
    filtered_data[filtered_data['disaster_type'] == 'Earthquake']['houses_damaged'].sum(),
    filtered_data[filtered_data['disaster_type'] == 'Flood / flash flood']['houses_damaged'].sum(),
    filtered_data[filtered_data['disaster_type'] == 'Heavy snowfall']['houses_damaged'].sum(),
    filtered_data[filtered_data['disaster_type'] == 'Landslide / mudflow']['houses_damaged'].sum()
], 0.4, label='Damaged', color='orange')
ax4.bar(x + 0.2, [
    filtered_data[filtered_data['disaster_type'] == 'Earthquake']['houses_destroyed'].sum(),
    filtered_data[filtered_data['disaster_type'] == 'Flood / flash flood']['houses_destroyed'].sum(),
    filtered_data[filtered_data['disaster_type'] == 'Heavy snowfall']['houses_destroyed'].sum(),
    filtered_data[filtered_data['disaster_type'] == 'Landslide / mudflow']['houses_destroyed'].sum()
], 0.4, label='Destroyed', color='red')
ax4.set_xticks(x)
ax4.set_xticklabels(['Earthquake', 'Flood / flash flood', 'Heavy snowfall', 'Landslide / mudflow'], rotation=45)
ax4.set_xlabel('Disaster Type')
ax4.set_ylabel('Number of Houses')
ax4.set_title('Houses Damaged vs Destroyed by Disaster Type')
ax4.legend()
st.pyplot(fig4)

st.markdown('---')

deaths_to_filter = st.slider('deaths', 0, 23, 5)
filtered_by_deaths = data[data['persons_killed'] == deaths_to_filter]
st.subheader('Incidents where deaths equal %s' % deaths_to_filter)
st.write(filtered_by_deaths)

st.markdown('---')

st.success('Dashboard loaded successfully!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.markdown('---')

st.caption('Data source: Humanitarian Data Exchange HDX Afghanistan Natural Disaster Incidents 2024')

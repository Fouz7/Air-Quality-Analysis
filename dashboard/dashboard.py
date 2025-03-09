import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='white')

all_df = pd.read_csv("df_all.csv")

# Convert 'date_time' column to datetime format
all_df['date_time'] = pd.to_datetime(all_df['date_time'])


st.header('Air Quality Analysis')
st.write('By Muhammad Dhiki Trilaksono F')

tab1, tab2, tab3 = st.tabs(["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])

with tab1:
    st.subheader("Bagaimana konsentrasi NO2 dan CO sebagai polutan dari kendaraan bermotor mempengaruhi kualitas udara?")
    all_df['date_time_month'] = all_df['date_time'].dt.to_period('M')

    monthly_avg = all_df.groupby('date_time_month').agg({
        'CO': 'mean',
        'NO2': 'mean',
        'PM2.5': 'mean',
        'PM10': 'mean',
        'SO2': 'mean',
        'O3': 'mean'
    }).reset_index()

    monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

    plt.figure(figsize=(14, 8))

    sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
    sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
    sns.lineplot(x='date_time_month', y='PM2.5', data=monthly_avg, label='PM2.5', color='purple')
    sns.lineplot(x='date_time_month', y='PM10', data=monthly_avg, label='PM10', color='pink')
    sns.lineplot(x='date_time_month', y='SO2', data=monthly_avg, label='SO2', color='orange')
    sns.lineplot(x='date_time_month', y='O3', data=monthly_avg, label='O3', color='green')

    plt.title('Rata-rata Bulanan Konsentrasi Polutan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Polutan')

    plt.xticks(ticks=monthly_avg['date_time_month'], labels=monthly_avg['date_time_month'].dt.strftime('%Y-%m'),
               rotation=45)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

    st.write("Konsentrasi CO dan NO₂ yang meningkat umumnya mencerminkan peningkatan aktivitas kendaraan bermotor atau pembakaran bahan bakar fosil. Ini mengindikasikan bahwa kendaraan bermotor dan bahan bakar fosil memiliki kontribusi signifikan terhadap polutan yang menyebabkan polusi udara.")

with tab2:
    st.subheader("Bagaimana hubungan antara polutan NO2 dan CO dengan pembentukan O3?")
    all_df['date_time_month'] = all_df['date_time'].dt.to_period('M')

    monthly_avg = all_df.groupby('date_time_month').agg({'NO2': 'mean', 'CO': 'mean', 'O3': 'mean'}).reset_index()

    monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

    plt.figure(figsize=(12, 6))

    sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
    sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
    sns.lineplot(x='date_time_month', y='O3', data=monthly_avg, label='O3', color='green')

    plt.title('Konsentrasi NO2, CO, dan O3 Bulanan')
    plt.xlabel('Bulan')
    plt.ylabel('Konsentrasi Polutan (NO2, CO, O3)')
    plt.legend()

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

    st.write("NO₂ dan CO berperan dalam pembentukan O₃. Ketika kadar NO₂ meningkat, kadar O₃ menurun, begitu pula sebaliknya. NO₂ dapat mengkatalisasi reaksi yang mengurangi konsentrasi O₃ di atmosfer. Di lingkungan dengan tingkat CO tinggi, reaksi yang membentuk O₃ dapat diperlambat.")

with tab3:
    st.subheader("Bagaimana hubungan antara polutan NO2 dan CO dengan PM2.5 dan PM10?")
    all_df['date_time_month'] = all_df['date_time'].dt.to_period('M')

    monthly_avg = all_df.groupby('date_time_month').agg({
        'NO2': 'mean',
        'CO': 'mean',
        'PM2.5': 'mean',
        'PM10': 'mean',
    }).reset_index()

    monthly_avg['date_time_month'] = monthly_avg['date_time_month'].dt.to_timestamp()

    plt.figure(figsize=(12, 6))

    sns.lineplot(x='date_time_month', y='NO2', data=monthly_avg, label='NO2', color='red')
    sns.lineplot(x='date_time_month', y='CO', data=monthly_avg, label='CO', color='blue')
    sns.lineplot(x='date_time_month', y='PM2.5', data=monthly_avg, label='PM2.5', color='purple')
    sns.lineplot(x='date_time_month', y='PM10', data=monthly_avg, label='PM10', color='pink')

    plt.title('Hub NO2, PM2.5, dan PM10')
    plt.xlabel('Periode')
    plt.ylabel('Konsentrasi Polutan (NO2, CO, PM2.5, dan PM10)')
    plt.legend()

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

    st.write("Naiknya kadar CO dan NO₂ menandakan intensitas aktivitas pembakaran yang tinggi. Hal ini berdampak pada peningkatan konsentrasi partikel-partikel udara, baik PM2.5 maupun PM10.")
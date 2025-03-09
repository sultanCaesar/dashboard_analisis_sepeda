import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


day_df = pd.read_csv('C:/Users/Asus/Documents/STUPEN DICODING/python only/projek_akhir/day.csv')
hour_df = pd.read_csv('C:/Users/Asus/Documents/STUPEN DICODING/python only/projek_akhir/hour.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

st.sidebar.title('Navigasi')
data_option = st.sidebar.radio("Pilih Tipe Data yang Ingin Dilihat:", ['Data Harian', 'Data Per Jam'])

st.title('Dashboard Analisis Pengguna Sepeda')

col1, col2 = st.columns(2)

if data_option == 'Data Harian':
    with col1:
        date_filter = st.slider(
            'Pilih Rentang Tanggal (Data Harian)',
            min_value=day_df['dteday'].min().to_pydatetime(),
            max_value=day_df['dteday'].max().to_pydatetime(),
            value=(day_df['dteday'].min().to_pydatetime(), day_df['dteday'].max().to_pydatetime())
        )

        filtered_data = day_df[(day_df['dteday'] >= date_filter[0]) & (day_df['dteday'] <= date_filter[1])]

    with col2:
        st.subheader('Tren Penjualan Sepeda Harian')
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=filtered_data, x='dteday', y='cnt', color='#4CAF50')
        plt.title('Tren Penjualan Sepeda Harian')
        plt.xlabel('Tanggal')
        plt.ylabel('Jumlah Pengguna Sepeda')
        st.pyplot(plt)

else:
    with col1:
        hour_filter = st.slider(
            'Pilih Rentang Tanggal (Data Per Jam)',
            min_value=hour_df['dteday'].min().to_pydatetime(),
            max_value=hour_df['dteday'].max().to_pydatetime(),
            value=(hour_df['dteday'].min().to_pydatetime(), hour_df['dteday'].max().to_pydatetime())
        )

        filtered_hour_data = hour_df[(hour_df['dteday'] >= hour_filter[0]) & (hour_df['dteday'] <= hour_filter[1])]

    with col2:
        st.subheader('Tren Penjualan Sepeda Per Jam')
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=filtered_hour_data, x='dteday', y='cnt', color='#4CAF50')
        plt.title('Tren Penjualan Sepeda Per Jam')
        plt.xlabel('Tanggal')
        plt.ylabel('Jumlah Pengguna Sepeda')
        st.pyplot(plt)

st.sidebar.subheader('Visualisasi Lainnya')
if st.sidebar.checkbox('Pengaruh Kondisi Cuaca'):
    st.subheader('Pengaruh Kondisi Cuaca terhadap Jumlah Pengguna Sepeda')
    weather_avg = day_df.groupby('weathersit')['cnt'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=weather_avg, x='weathersit', y='cnt', palette='coolwarm')
    plt.title('Jumlah Pengguna Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)

if st.sidebar.checkbox('Perbandingan Musim'):
    st.subheader('Perbandingan Jumlah Pengguna Sepeda Berdasarkan Musim')
    season_avg = day_df.groupby('season')['cnt'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=season_avg, x='season', y='cnt', palette='viridis')
    plt.title('Jumlah Pengguna Sepeda Berdasarkan Musim')
    plt.xlabel('Musim (1=Semi, 2=Panas, 3=Gugur, 4=Dingin)')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)

if st.sidebar.checkbox('Perbandingan Hari Kerja vs Hari Libur'):
    st.subheader('Perbandingan Jumlah Pengguna Sepeda pada Hari Kerja vs Hari Libur')
    workday_avg = day_df.groupby('workingday')['cnt'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=workday_avg, x='workingday', y='cnt', palette='Set2')
    plt.title('Jumlah Pengguna Sepeda pada Hari Kerja vs Hari Libur')
    plt.xlabel('0 = Libur, 1 = Hari Kerja')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)

st.markdown("---")
st.markdown("**Dashboard ini dibuat Oleh Sultan Caesar Al-zaky.**")

import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_echarts import st_echarts
import matplotlib.pyplot as plt

with st.sidebar :
    selected = option_menu ('Hitung Luas Bangun',
    ['Hitung Luas Lingkaran','Hitung Luas Persegi Panjang',
    'Hitung Luas Segitiga', 'Hitung Luas Trapesium', 'Hitung Luas Jajar Genjang', 'Hitung Luas Layang-Layang', 'Hitung Luas Belah Ketupat'],
    default_index=0)
    
if selected == 'Hitung Luas Lingkaran':
    st.title('Hitung Luas Lingkaran')

    radius = st.slider("Masukkan Nilai Jari-jari", 0)
    hitung = st.button("Hitung Luas Lingkaran")

    if hitung:
        luas = 3.14 * radius * radius
        st.write("Luas Lingkaran adalah =", luas)
        st.success(f"Luas Lingkaran adalah = {luas}")

    fig, ax = plt.subplots()
    circle = plt.Circle((0.5, 0.5), radius, fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim([0, 2 * radius + 1])
    ax.set_ylim([0, 2 * radius + 1])
    ax.set_aspect('equal', adjustable='box')
    st.pyplot(fig)

if (selected == 'Hitung Luas Persegi Panjang') : 
    st.title('Hitung Luas Persegi Panjang')

    panjang = st.number_input ("Masukan Nilai Panjang", 0)
    lebar = st.number_input ("Masukan NIlai Lebar", 0)
    hitung = st.button ("Hitung Luas Persegi Panjang")

    if hitung :
        luas = panjang * lebar
        st.write ("Luas Persegi Panjgan Adalah = ", luas)
        st.success (f"Luas Persegi Panjang Adalah = {luas}")
        
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), panjang, lebar, fill=False, edgecolor='blue', linewidth=2))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([0, max(panjang, lebar) + 5])
    ax.set_ylim([0, max(panjang, lebar) + 5])
    st.pyplot(fig)
        
if (selected == 'Hitung Luas Segitiga') :
    st.title('Hitung Luas Segitiga')
    
    alas = st.number_input ("Masukan Nilai Alas", 0, 100)
    tinggi = st.number_input ("Masukan Nilai Tinggi", 0, 100)
    hitung = st.button ("Hitung Luas Segitiga")
    
    if hitung :
        luas = 0.5 * alas * tinggi
        st.write ("Luas Segitiga Adalah = ", luas)
        st.success (f"Luas Segitiga Adalah = {luas}")
        
    fig, ax = plt.subplots()
    ax.add_patch(plt.Polygon([[0, 0], [alas, 0], [0.5 * alas, tinggi]], closed=True, fill=False, edgecolor='blue', linewidth=2))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([0, max(alas, tinggi) + 5])
    ax.set_ylim([0, max(alas, tinggi) + 5])
    st.pyplot(fig)

if selected == 'Hitung Luas Trapesium':
    st.title('Hitung Luas Trapesium')

    sisi_a = st.number_input("Masukkan Panjang Sisi A", 0)
    sisi_b = st.number_input("Masukkan Panjang Sisi B", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas Trapesium")

    if hitung:
        luas = (sisi_a + sisi_b) * tinggi / 2
        st.write("Luas Trapesium adalah =", luas)
        st.success(f"Luas Trapesium adalah = {luas}")

    fig, ax = plt.subplots()
    ax.add_patch(plt.Polygon([[0, 0], [sisi_a, 0], [sisi_b, tinggi], [0, tinggi]], fill=False, edgecolor='blue', linewidth=2))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([0, max(sisi_a, sisi_b) + 5])
    ax.set_ylim([0, tinggi + 5])
    st.pyplot(fig)
    
if selected == 'Hitung Luas Jajar Genjang':
    st.title('Hitung Luas Jajar Genjang')

    alas = st.number_input("Masukkan Panjang Alas", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas Jajar Genjang")

    if hitung:
        luas = alas * tinggi
        st.write("Luas Jajar Genjang adalah =", luas)
        st.success(f"Luas Jajar Genjang adalah = {luas}")

    fig, ax = plt.subplots()
    ax.add_patch(plt.Polygon([[0, 0], [alas, 0], [alas, tinggi], [0, tinggi]], fill=False, edgecolor='blue', linewidth=2))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([0, alas + 5])
    ax.set_ylim([0, tinggi + 5])
    st.pyplot(fig)
    
if selected == 'Hitung Luas Layang-Layang':
    st.title('Hitung Luas Layang-Layang')

    diagonal_1 = st.number_input("Masukkan Panjang Diagonal 1", 0)
    diagonal_2 = st.number_input("Masukkan Panjang Diagonal 2", 0)
    hitung = st.button("Hitung Luas Layang-Layang")

    if hitung:
        luas = (diagonal_1 * diagonal_2) / 2
        st.write("Luas Layang-Layang adalah =", luas)
        st.success(f"Luas Layang-Layang adalah = {luas}")

    fig, ax = plt.subplots()
    ax.add_patch(plt.Polygon([[0, 0], [diagonal_1, 0], [0, diagonal_2], [-diagonal_1, 0]], fill=False, edgecolor='blue', linewidth=2))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([-diagonal_1 - 5, diagonal_1 + 5])
    ax.set_ylim([-diagonal_2 - 5, diagonal_2 + 5])
    st.pyplot(fig)

if selected == 'Hitung Luas Belah Ketupat':
    st.title('Hitung Luas Belah Ketupat')

    diagonal_1 = st.number_input("Masukkan Panjang Diagonal 1", 0)
    diagonal_2 = st.number_input("Masukkan Panjang Diagonal 2", 0)
    hitung = st.button("Hitung Luas Belah Ketupat")

    if hitung:
        luas = (diagonal_1 * diagonal_2) / 2
        st.write("Luas Belah Ketupat adalah =", luas)
        st.success(f"Luas Belah Ketupat adalah = {luas}")

    fig, ax = plt.subplots()
    ax.add_patch(plt.Polygon([[0, 0], [diagonal_1 / 2, diagonal_2 / 2], [0, diagonal_2], [-diagonal_1 / 2, diagonal_2 / 2]], fill=False, edgecolor='blue', linewidth=2))
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([-diagonal_1 / 2 - 5, diagonal_1 / 2 + 5])
    ax.set_ylim([-diagonal_2 / 2 - 5, diagonal_2 + 5])
    st.pyplot(fig)
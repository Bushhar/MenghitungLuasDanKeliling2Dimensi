import streamlit as st 
import pandas as pd
import numpy as np 
from streamlit_option_menu import option_menu
from streamlit_echarts import st_echarts
import matplotlib.pyplot as plt

option_list = ['Luas', 'Keliling']

with st.sidebar:
    selected_option = st.selectbox('Pilih Opsi', option_list)

with st.sidebar:
    selected_shape = st.selectbox('Pilih Bangun 2D', ['Persegi Panjang', 'Segitiga', 'Lingkaran', 'Trapesium', 'Jajar Genjang', 'Belah Ketupat', 'Layang-Layang'])

if selected_option == 'Luas':
    st.title('Hitung Luas Bangun')

    if selected_shape == 'Persegi Panjang':
        st.subheader('Persegi Panjang')
        panjang = st.number_input("Masukkan Nilai Panjang", 0)
        lebar = st.number_input("Masukkan NIlai Lebar", 0)
        hitung = st.button("Hitung Luas")

        if hitung:
            luas = panjang * lebar
            st.write("Luas Persegi Panjang adalah =", luas)
            st.success(f"Luas Persegi Panjang adalah = {luas}")

        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), panjang, lebar, fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([0, max(panjang, lebar) + 5])
        ax.set_ylim([0, max(panjang, lebar) + 5])
        st.pyplot(fig)

    elif selected_shape == 'Lingkaran':
        st.subheader('Lingkaran')
        radius = st.slider("Masukkan Nilai Jari-jari", 0)
        hitung = st.button("Hitung Luas")

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
    
    elif selected_shape == 'Segitiga' :
        st.subheader('Segitiga')
        
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
        
    elif selected_shape == 'Trapesium':
        st.subheader('Trapesium')

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
    
    elif selected_shape == 'Jajar Genjang':
        st.subheader('Jajar Genjang')

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
    
    elif selected_shape == 'Belah Ketupat':
        st.subheader('Belah Ketupat')

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
        
    elif selected_shape == 'Layang-Layang':
        st.subheader('Layang-Layang')

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
        
elif selected_option == 'Keliling':
    st.title('Hitung Keliling Bangun')

    if selected_shape == 'Persegi Panjang':
        st.subheader('Persegi Panjang')
        panjang = st.number_input("Masukkan Nilai Panjang", 0)
        lebar = st.number_input("Masukkan NIlai Lebar", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = 2 * (panjang + lebar)
            st.write("Keliling Persegi Panjang adalah =", keliling)
            st.success(f"Keliling Persegi Panjang adalah = {keliling}")

        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), panjang, lebar, fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([0, max(panjang, lebar) + 5])
        ax.set_ylim([0, max(panjang, lebar) + 5])
        st.pyplot(fig)

    elif selected_shape == 'Lingkaran':
        st.subheader('Lingkaran')
        radius = st.slider("Masukkan Nilai Jari-jari", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = 2 * 3.14 * radius
            st.write("Keliling Lingkaran adalah =", keliling)
            st.success(f"Keliling Lingkaran adalah = {keliling}")

        fig, ax = plt.subplots()
        circle = plt.Circle((0.5, 0.5), radius, fill=False, edgecolor='blue', linewidth=2)
        ax.add_patch(circle)
        ax.set_xlim([0, 2 * radius + 1])
        ax.set_ylim([0, 2 * radius + 1])
        ax.set_aspect('equal', adjustable='box')
        st.pyplot(fig)

    elif selected_shape == 'Segitiga':
        st.subheader('Segitiga')

        sisi_a = st.number_input("Masukkan Panjang Sisi A", 0)
        sisi_b = st.number_input("Masukkan Panjang Sisi B", 0)
        sisi_c = st.number_input("Masukkan Panjang Sisi C", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = sisi_a + sisi_b + sisi_c
            st.write("Keliling Segitiga adalah =", keliling)
            st.success(f"Keliling Segitiga adalah = {keliling}")

        fig, ax = plt.subplots()
        ax.add_patch(
            plt.Polygon([[0, 0], [sisi_a, 0], [sisi_c, sisi_b]], closed=True, fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([0, max(sisi_a, sisi_b, sisi_c) + 5])
        ax.set_ylim([0, max(sisi_a, sisi_b, sisi_c) + 5])
        st.pyplot(fig)
        
    elif selected_shape == 'Trapesium':
        st.subheader('Trapesium')

        sisi_a = st.number_input("Masukkan Panjang Sisi A", 0)
        sisi_b = st.number_input("Masukkan Panjang Sisi B", 0)
        sisi_c = st.number_input("Masukkan Panjang Sisi C", 0)
        sisi_d = st.number_input("Masukkan Panjang Sisi D", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = sisi_a + sisi_b + sisi_c + sisi_d
            st.write("Keliling Trapesium adalah =", keliling)
            st.success(f"Keliling Trapesium adalah = {keliling}")

        fig, ax = plt.subplots()
        ax.add_patch(
            plt.Polygon([[0, 0], [sisi_a, 0], [sisi_c, 0], [sisi_d, sisi_b]], fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([0, max(sisi_a, sisi_b, sisi_c, sisi_d) + 5])
        ax.set_ylim([0, max(sisi_a, sisi_b, sisi_c, sisi_d) + 5])
        st.pyplot(fig)

    elif selected_shape == 'Jajar Genjang':
        st.subheader('Jajar Genjang')

        sisi_a = st.number_input("Masukkan Panjang Sisi A", 0)
        sisi_b = st.number_input("Masukkan Panjang Sisi B", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = 2 * (sisi_a + sisi_b)
            st.write("Keliling Jajar Genjang adalah =", keliling)
            st.success(f"Keliling Jajar Genjang adalah = {keliling}")

        fig, ax = plt.subplots()
        ax.add_patch(
            plt.Polygon([[0, 0], [sisi_a, 0], [sisi_a + sisi_b, sisi_b], [sisi_b, sisi_b]], fill=False, edgecolor='blue',
                        linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([0, sisi_a + sisi_b + 5])
        ax.set_ylim([0, max(sisi_a, sisi_b) + 5])
        st.pyplot(fig)
        
    elif selected_shape == 'Belah Ketupat':
        st.subheader('Belah Ketupat')

        sisi = st.number_input("Masukkan Panjang Sisi", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = 4 * sisi
            st.write("Keliling Belah Ketupat adalah =", keliling)
            st.success(f"Keliling Belah Ketupat adalah = {keliling}")

        fig, ax = plt.subplots()
        ax.add_patch(plt.Polygon([[0, sisi], [sisi, 0], [2 * sisi, sisi], [sisi, 2 * sisi]], fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([0, 2 * sisi + 5])
        ax.set_ylim([0, 2 * sisi + 5])
        st.pyplot(fig)
        
    elif selected_shape == 'Layang-Layang':
        st.subheader('Layang-Layang')

        sisi_a = st.number_input("Masukkan Panjang Sisi A", 0)
        sisi_b = st.number_input("Masukkan Panjang Sisi B", 0)
        hitung = st.button("Hitung Keliling")

        if hitung:
            keliling = 2 * (sisi_a + sisi_b)
            st.write("Keliling Layang-Layang adalah =", keliling)
            st.success(f"Keliling Layang-Layang adalah = {keliling}")

        fig, ax = plt.subplots()
        ax.add_patch(plt.Polygon([[0, 0], [sisi_a, 0], [0, sisi_b], [-sisi_a, 0]], fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim([-sisi_a - 5, sisi_a + 5])
        ax.set_ylim([-sisi_b - 5, sisi_b + 5])
        st.pyplot(fig)

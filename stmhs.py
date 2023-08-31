import streamlit as st
import sqlite3

# Fungsi untuk melakukan operasi UPDATE pada data mahasiswa
def update_student(nim, nama, jenis_kelamin, kd_jurusan):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('UPDATE students SET nama=?, jenis_kelamin=?, kd_jurusan=? WHERE nim=?',
              (nama, jenis_kelamin, kd_jurusan, nim))
    conn.commit()
    conn.close()

# Fungsi untuk mendapatkan data mahasiswa berdasarkan NIM
def get_student_by_nim(nim):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE nim=?', (nim,))
    student = c.fetchone()
    conn.close()
    return student

# Main
def main():
    st.title("Aplikasi Data Mahasiswa")
    
       
    nim = st.text_input("NIM:")
    if nim:
        student = get_student_by_nim(nim)
        if student:
            st.write("Data Mahasiswa:")
            st.write(f"NIM: {student[0]}, Nama: {student[1]}, Jenis Kelamin: {student[2]}, Kode Jurusan: {student[3]}")
            nama = st.text_input("Nama:", student[1])
            jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Laki-laki", "Perempuan"], index=0 if student[2] == "Laki-laki" else 1)
            kd_jurusan = st.text_input("Kode Jurusan:", student[3])
            if st.button("Update"):
                update_student(nim, nama, jenis_kelamin, kd_jurusan)
                st.success("Data mahasiswa diperbarui!")

if __name__ == '__main__':
    main()

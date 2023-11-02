nilai_murid = [60, 70, 85, 90, 25]
jumlah_nilai = len(nilai_murid)

if jumlah_nilai > 0: 
    mean = sum(nilai_murid) / jumlah_nilai
    print("Mean (rata-rata) adalah:", mean)
else:
    print("Daftar nilai kosong.") 

daftar_obat = {
    "m01": ("Paracetamol", 5000),
    "m02": ("Antasida", 8000),
    "m03": ("Oralit", 3000),
    "m04": ("Cetirizine", 7000),
    "m05": ("Vitamin C", 10000),
    "m06": ("Obat batuk", 12000),
    "m07": ("Balsem", 14500),
    "m08": ("Betadine", 16000),
    "m09": ("Minyak kayu putih", 13500),
    "m10": ("Obat flu", 15000),
}

daftar_pasien = {
    "p01": ("Demam", 2),
    "p02": ("Flu", 3),
    "p03": ("Diare", 4),
    "p04": ("Maag", 2),
    "p05": ("Alergi", 3),
    "p06": ("Infeksi", 5),
    "p07": ("Gangguan pernapasan", 6),
    "p08": ("Tifus", 7),
    "p09": ("DBD", 8),
    "p10": ("Pemulihan pascaoperasi", 10),
}

print("""
========================================
          SISTEM APOTEK DEWI
========================================
           DAFTAR NAMA OBAT
========================================
Kode   Nama Obat              Harga
========================================
""")

for kode, data in daftar_obat.items():
    print(f"{kode}    {data[0]:22} Rp {data[1]:,}")

print("""
========================================
          DAFTAR PASIEN OPNAME
========================================
Kode   Jenis Penyakit
========================================
""")

for kode, data in daftar_pasien.items():
    print(f"{kode}    {data[0]}")

print("========================================")

# INPUT DATA PASIEN

kode_pasien = input("Masukkan kode pasien = ").lower()

if kode_pasien in daftar_pasien:

    nama_penyakit, hari_opname = daftar_pasien[kode_pasien]

    print("\n========================================")
    print("           DATA PASIEN")
    print("========================================")
    print("Penyakit       :", nama_penyakit)

    hari_opname = int(input("Lama opname (hari) = "))

    keranjang = []
    pilihan = "y"

    # INPUT PEMBELIAN OBAT

    while pilihan.lower() == "y":

        pesan = input("\nMasukkan kode obat = ").lower()

        if pesan not in daftar_obat:
            print("Kode obat tidak terdaftar!")
            continue

        nama_obat, harga_satuan = daftar_obat[pesan]

        jumlah = int(input("Jumlah obat = "))

        harga = harga_satuan * jumlah

        # OPERATOR KONDISIONAL DISKON OBAT

        if pesan == "m01" and jumlah >= 10:
            diskon = harga * 0.10

        elif pesan == "m02" and jumlah >= 5:
            diskon = harga * 0.05

        elif pesan == "m05" and jumlah >= 5:
            diskon = harga * 0.05

        elif pesan == "m07" and jumlah >= 5:
            diskon = harga * 0.05

        elif pesan == "m10" and jumlah >= 5:
            diskon = harga * 0.05

        else:
            diskon = 0

        total = harga - diskon

        keranjang.append({
            "nama": nama_obat,
            "jumlah": jumlah,
            "harga": harga,
            "diskon": diskon,
            "total": total
        })

        pilihan = input(
            "\nApakah ingin membeli obat lain? Y/N = "
        )

    # PERHITUNGAN TOTAL

    grand_total = 0

    print("\n========================================")
    print("             STRUK APOTEK")
    print("========================================")
    print("Penyakit       :", nama_penyakit)
    print("Lama opname    :", hari_opname, "hari")
    print("----------------------------------------")

    for item in keranjang:
        print(item["nama"], "x", item["jumlah"])
        print("Harga  : Rp", int(item["harga"]))
        print("Diskon : Rp", int(item["diskon"]))
        print("Total  : Rp", int(item["total"]))
        print("----------------------------------------")

        grand_total += item["total"]

    # DISKON PASIEN OPNAME

    if hari_opname > 3:
        diskon_pasien = grand_total * 0.05
    else:
        diskon_pasien = 0

    total_bayar = grand_total - diskon_pasien

    print("Total obat       : Rp", int(grand_total))
    print("Diskon pasien    : Rp", int(diskon_pasien))
    print("----------------------------------------")
    print("TOTAL BAYAR      : Rp", int(total_bayar))
    print("========================================")
    print("       TERIMA KASIH")
    print("========================================")

else:
    print("Kode pasien tidak terdaftar!")

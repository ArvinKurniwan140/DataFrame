import pandas as pd

df = pd.read_csv('iniDF.csv', usecols=["nama_kabupaten_kota", "jumlah_produksi_sampah", "satuan", "tahun"])

total = 0
tahun = 2017
for i, j in df.iterrows():
    if j['tahun'] == 2017:
        total += j['jumlah_produksi_sampah']

print(f"Total Produksi sampah tahun 2017 = {total}")

dfTotal = pd.DataFrame([{
    'Tahun': tahun,
    'Total Produksi Sampah (ton)': total
}])

csv_file = 'total_produksi_sampah2017.csv'
dfTotal.to_csv(csv_file, index=False)

excel_file = 'total_produksi_sampah2017.xlsx'
dfTotal.to_excel(excel_file, index=False)


total_sampah_pertahun = {}
for k, l in df.iterrows():
    tahun = l['tahun']
    sampah = l['jumlah_produksi_sampah']

    if tahun in total_sampah_pertahun:
        total_sampah_pertahun[tahun] += sampah
    else:
        total_sampah_pertahun[tahun] = sampah

print(total_sampah_pertahun)
dfPertahun = pd.DataFrame(list(total_sampah_pertahun.items()), columns=['Tahun', 'Total Produksi Sampah (ton)'])

csv_file = 'total_produksi_sampah.csv'
dfPertahun.to_csv(csv_file, index=False)

excel_file = 'total_produksi_sampah.xlsx'
dfPertahun.to_excel(excel_file, index=False)

total_perTahunKab = {}
for m, n in df.iterrows():
    kab = (n['nama_kabupaten_kota'], n['tahun'])
    sampah = n['jumlah_produksi_sampah']

    if kab in total_perTahunKab:
        total_perTahunKab[kab] += sampah
    else:
        total_perTahunKab[kab] = sampah

print(total_perTahunKab)

dfPerKabTahun = pd.DataFrame(
    [(kota, tahun, total) for (kota, tahun), total in total_perTahunKab.items()],
    columns=['Kabupaten/Kota', 'Tahun', 'Total Produksi Sampah (ton)']
)

csv_file = 'total_produksi_sampahTahunKab.csv'
dfPerKabTahun.to_csv(csv_file, index=False)

excel_file = 'total_produksi_sampahTahunKab.xlsx'
dfPerKabTahun.to_excel(excel_file, index=False)

data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

def tampilkan_hasil_panen(data):
    print("")
    for lokasi in data:
        print("Lokasi:", data[lokasi]["nama_lokasi"])
        print("Hasil Panen:")
        print("  Padi:", data[lokasi]["hasil_panen"]["padi"])
        print("  Jagung:", data[lokasi]["hasil_panen"]["jagung"])
        print("  Kedelai:", data[lokasi]["hasil_panen"]["kedelai"])
        print()

    print("")
    lokasi2 = data["lokasi2"]
    print("Lokasi:", lokasi2["nama_lokasi"])
    print("Hasil Panen Jagung:", lokasi2["hasil_panen"]["jagung"])
    print()

    print("")
    lokasi3 = data["lokasi3"]
    print("Nama Lokasi dari lokasi3 adalah", lokasi3["nama_lokasi"])
    print()


    print("")
    total_padi = 0
    total_kedelai = 0
    for lokasi in data:
        total_padi += data[lokasi]["hasil_panen"]["padi"]
        total_kedelai += data[lokasi]["hasil_panen"]["kedelai"]
    print("Total Hasil Panen Padi:", total_padi)
    print("Total Hasil Panen Kedelai:", total_kedelai)
    print()

    print("")
    for lokasi in data:
        print("Lokasi:", data[lokasi]["nama_lokasi"])
        print("  Padi:", data[lokasi]["hasil_panen"]["padi"])
        print("  Jagung:", data[lokasi]["hasil_panen"]["jagung"])
        print("  Kedelai:", data[lokasi]["hasil_panen"]["kedelai"])
        print()

    print("")
    for lokasi in data:
        padi = data[lokasi]["hasil_panen"]["padi"]
        jagung = data[lokasi]["hasil_panen"]["jagung"]
        if padi > 1300 or jagung > 800:
            print("Lokasi", data[lokasi]["nama_lokasi"], "memerlukan perhatian khusus.")
        else:
            print("Lokasi", data[lokasi]["nama_lokasi"], "dalam kondisi baik.")
    print()

tampilkan_hasil_panen(data_panen)

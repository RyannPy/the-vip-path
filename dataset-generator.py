import pandas as pd
import numpy as np

def pelanggan_generator(n_pelanggan=1000):
    np.random.seed(42)

    data = []

    for id_pelanggan in range(1, n_pelanggan+1):
        # 1. JAM MAIN MINGGUAN
        jam_main_mingguan = round(np.random.uniform(1, 60), 2)

        # 2. GENRE FAVORIT
        genre_favorit = np.random.choice(["FPS", "MOBA", "RPG", "Casual"])

        # 3. SNACK
        pengeluaran_snack = round(np.random.uniform(5, 100)) * 1000

        # 4. WAKTU MAIN UTAMA
        if genre_favorit == "RPG": # player rpg lebih sering main saat malam atau subuh
            waktu_main_utama = np.random.choice(["Pagi", "Siang", "Sore", "Malam", "Subuh"], p=[0.05, 0.1, 0.15, 0.4, 0.3])
        else: 
            waktu_main_utama = np.random.choice(["Pagi", "Siang", "Sore", "Malam", "Subuh"])

        # 5. HARDWARE
        if genre_favorit in ["FPS", "MOBA"] : # player fps mencari hardware bagus
            hardware_requirement = np.random.choice([0, 1], p=[0.2, 0.8])
        else:
            hardware_requirement = np.random.choice([0, 1], p=[0.7, 0.3])

        # 6. VIP LOUNGE VISIT
        vip_lounge_visit = 0
        if jam_main_mingguan > 30:
            vip_lounge_visit = np.random.randint(5, 25)
        else:
            vip_lounge_visit = np.random.randint(0, 5)

        

        # 7. MEMBERSHIP?
        prob_membership = 0.05 # base


       # Skenario 1: Si Hardcore (FPS/MOBA + Hardware + Jam Main)
        if genre_favorit in ["FPS", "MOBA"] and hardware_requirement == 1 and jam_main_mingguan > 35:
            prob_membership += 0.8
        
        # Skenario 2: Si Sultan (Casual + Snack Tinggi)
        elif genre_favorit == "Casual" and pengeluaran_snack > 70000:
            prob_membership += 0.7
        
        # Skenario 3: Si Nocturnal (RPG + Malam/Subuh)
        elif genre_favorit == "RPG" and waktu_main_utama in ["Malam", "Subuh"]:
            prob_membership += 0.5

        # noise
        target_membership = np.random.choice([0, 1], p=[max(0, 1-prob_membership), min(1, prob_membership)])

        data.append({
            "id_pelanggan": id_pelanggan,
            "jam_main_mingguan": jam_main_mingguan,
            "genre_favorit": genre_favorit,
            "pengeluaran_snack": pengeluaran_snack,
            "waktu_main_utama": waktu_main_utama,
            "hardware_requirement": hardware_requirement,
            "vip_lounge_visit": vip_lounge_visit,
            "target_membership": target_membership,
        })
        

    return pd.DataFrame(data)

df = pelanggan_generator(1000)

    

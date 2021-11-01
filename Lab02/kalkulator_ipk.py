# declare variable
sum_sks_lulus = 0
sum_sks_not_lulus = 0
mutu = 0
mutu_not_lulus=0
total = 0
total_not_lulus = 0

print("Selamat datang di kalkulator IPK!\n")
jumlah_matkul = int(input("Masukkan Jumlah Mata Kuliah yang Diambil : "))

while jumlah_matkul < 0:  # while jumlah matkul is still not valid it will keep asKing the right value
    print('Tolong Masukkan Jumlah Mata Kuliah yang benar')
    jumlah_matkul = int(input("Masukkan Jumlah Mata Kuliah yang Diambil : "))

# check whether jumlah_matkul is positive number and not 0, if zero then return tidak ada matkul yang diambil
if jumlah_matkul > 0:    
    # loop as many as jumlah matkul
    for x in range(jumlah_matkul): 
        mata_kuliah = input(f"Masukkan Nama Mata Kuliah ke-{x+1} : ") 
        jumlah_sks = int(input(f"Masukkan Jumlah SKS Mata Kuliah {mata_kuliah} : "))

        nilai=float(input(f"Masukkan Nilai Mata Kuliah {mata_kuliah}: "))

    # check if nilai is negative or not. if negative ask again the valid number
        while nilai < 0:
            print('\nNilai yang Kamu Masukkan Tidak Valid')
            nilai=float(input(f"Masukkan Nilai Mata Kuliah {mata_kuliah}: "))
        print("\n=================================\n")
    # if nilai bigger than 85 so give bobot 4, then add jumlah_sks to the variable sum_sks_lulus 
    # then bobot*jumlah sks and the add the value to total so we can sum up all the mutu
    # this logics applied to all of the conditional 
        if nilai >= 55:
            if nilai >= 85:
                bobot = 4 
            elif nilai >= 80 and nilai < 85:
                bobot = 3.7 
            elif nilai >= 75 and nilai < 80:
                bobot = 3.3 
            elif nilai >= 70 and nilai < 75:
                bobot = 3 
            elif nilai >= 65 and nilai < 70:
                bobot = 2.7    
            elif nilai >= 60 and nilai < 65:
                bobot = 2.3 
            elif nilai >= 55 and nilai < 60:
                bobot = 2 
            sum_sks_lulus += jumlah_sks
            mutu = bobot * jumlah_sks
            total += mutu
        elif nilai >= 0 and nilai < 55:
            # if not lulus then add jumlah sks to the variable sum_sks_not lulus so we can sum up how many sks is not passed.     
            if nilai >= 40 and nilai < 55: 
                bobot = 1
            elif nilai >= 0 and nilai < 40:
                bobot = 0
            sum_sks_not_lulus += jumlah_sks
            mutu_not_lulus = bobot * jumlah_sks
            total_not_lulus += mutu_not_lulus
    

    print("Rekapitulasi Nilai: ")
    # there is probability that student is not passed all of the matkul so
    # if the total sks lulus is zero then return IPK and IPT zero    
    if sum_sks_lulus == 0:
        ipt = (total+ total_not_lulus) / (sum_sks_lulus+sum_sks_not_lulus)
        print(f'Jumlah SKS Lulus {sum_sks_lulus} / {sum_sks_lulus+sum_sks_not_lulus}')        # get the amount of sum_sks_lulus and get the amount of sks_total that is sks_lulus+sks not lulus
        print(f'Jumlah Mutu Lulus {total:.2f} / {(total+total_not_lulus):.2f}')
        print(f'Total IPK kamu adalah: 0.00')
        print(f'Total IPT kamu adalah: {ipt:.2f}')

    # else if there are sks lulus then execute the following statement
    else:
        ipk = total / sum_sks_lulus
        ipt = (total+ total_not_lulus) / (sum_sks_lulus+sum_sks_not_lulus)

        print(f'Jumlah SKS Lulus {sum_sks_lulus} / {sum_sks_lulus+sum_sks_not_lulus}')      # get the amount of sum_sks_lulus and get the amount of sks_total that is sks_lulus+sks not lulus
        print(f'Jumlah Mutu Lulus {total:.2f} / {(total+total_not_lulus):.2f}')             # get the amount of mutu_lulus and get the amount of mutu total that is mutu_lulus+mutu not lulus
        print(f'Total IPK kamu adalah: {ipk:.2f}')
        print(f'Total IPT kamu adalah: {ipt:.2f}')
elif jumlah_matkul == 0:
    print('Tidak ada mata kuliah yang diambil')

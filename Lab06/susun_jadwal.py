from operator import itemgetter

def integer_to_schedule(time):
    # get day, time floor divison with 24*60
    day = time // MENIT_DALAM_HARI    
    # and then we should multiply the day and 24*60 then substract with time and we got the remaining time  
    remaining = time - MENIT_DALAM_HARI * day
    # get hour, remaining floor division with 60
    hour = remaining // MENIT_DALAM_JAM
    # and then multiply the hour and 60 then substract with remaining time 
    minute = remaining - MENIT_DALAM_JAM * hour
    # declare days
    list_hari = [
        "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"
    ]
    # if minute 0--9 then we should add "0" so it will return 9:00 example rather than 9:0
    if minute < 10: 
        minute = "0" + str(minute)
    # return to the function call day, hour and minute
    return f"{list_hari[day]}, {hour}.{minute}"


MENIT_DALAM_JAM = 60 
MENIT_DALAM_HARI = 60 * 24

HARI = [i * MENIT_DALAM_HARI for i in range(7)]
JAM = [i * MENIT_DALAM_JAM for i in range(24)]

MATKUL_TERSEDIA = [
["ddp 1 a", HARI[0] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["ddp 1 a", HARI[1] + JAM[8] + 0, HARI[0] +  JAM[9] + 40],
["manbis", HARI[4] + JAM[13] + 1, HARI[4] + JAM[15] + 40],
["matdis 1 a", HARI[4] + JAM[9] + 0, HARI[4] + JAM[13] + 0],
["matdis 1 b", HARI[2] + JAM[9] + 0, HARI[2] + JAM[10] + 40],
["kalkulus 1 c", HARI[2] + JAM[10] + 0, HARI[2] + JAM[12] + 00]
]
"""
Merepresentasikan jadwal “ddp 1 a” hari senin 08.00 sampai 09.40, serta hari rabu jam 08.00 sampai 09.40

Jadwal “ddp 1 b” hari selasa jam 08.00 sampai 09.40
Jadwal “manbis” hari senin jam 09.00 sampai 10.40
Jadwal “matdis 1 a” hari rabu jam 09.00 sampai 10.40
Jadwal “matdis 1 b” hari rabu jam 09.00 sampai 10.40
"""



# declare variable
matkul_pilihan = []
bentrok = False

# while its not stopped then it will execute the next lines
while True:
    print("=" * 15, "SUSUN JADWAL", "=" * 15)
    print("1  Add matkul")
    print("2  Drop matkul")
    print("3  Cek ringkasan")
    print("4  Lihat daftar matkul")
    print("5  Selesai")
    print("=" * 44)

    choice = input("Masukkan pilihan: ")
    # delete leading and trailing space
    choice.strip()
    # if user choose one then execute next lines
    if choice == "1":
        nama_matkul = input("Masukkan nama matkul: ")
        # matkul_added is a list containing matkul that's in matkul tersedia
        # case insensitive so we need to lower and for the input we need to extra strip to remove leading and trailing space
        matkul_added = [
            matkul for matkul in MATKUL_TERSEDIA
            if nama_matkul.lower().strip() == matkul[0].lower() #matkul[0] is the name of matkul in matkul tersedia 
        ]
        # if there's matkul in list matkul tersedia then add to the list matkul pilihan 
        print(matkul_added)
        if matkul_added != []:
            matkul_pilihan.extend(matkul_added)
        # else please return matkul not found
        else:
            print("Matkul tidak ditemukan")
    # if user choose two then execute this next lines
    elif choice == "2":
        nama_matkul = input("Masukkan nama matkul: ")
        # find the matching nama matkul
        # also case insensitive so we need to lower
        matkul_removed = [
            matkul for matkul in matkul_pilihan
            if nama_matkul.lower().strip() == matkul[0].lower()#matkul[0] is the name of matkul in matkul tersedia 
        ]
        # if there's matkul match then remove the item, we need to iterate incase there's two schedules or more in the matkul
        # so all removed
        if matkul_removed != []:
            for remove_item in matkul_removed:
                matkul_pilihan.remove(remove_item)
        else:
            print("Matkul tidak ditemukan")

    # if choose 3 then we need to check if its conflict schedule or not
    elif choice == "3":
        # this nested loop is to check in every matakuliah we have there's no conflict with each other
        for mata_kuliah in matkul_pilihan:
            for matkul in matkul_pilihan:
                # if its same mata kuliah then skip the checking 
                if mata_kuliah[0] == matkul[0]:
                    continue
                # if its different mata kuliah and it is conflicted then assign bentrok to true
                # conflicted when the mata kuliah time intersect with another mata kuliah
                elif mata_kuliah[0] != matkul[0] and mata_kuliah[1] <= matkul[
                        1] <= mata_kuliah[2]:
                    bentrok = True
                    print(f"{mata_kuliah[0]} bentrok dengan {matkul[0]}")
        # if not bentrok then execute this next line
        if not bentrok:
            print("tidak ada matkul yang bermasalah")
        # reset the bentrok statement
        bentrok = False

        # if choose 4 then it will return the list of mata kuliah selected
    elif choice == "4":
        # if empty matkul then return no matkul selected
        if matkul_pilihan == []:
            print("Tidak ada matkul yang diambil")
        else:
        # else print the schedule
        # first we need to sort by minutes, the less minutes will be shown first
        # matkul pilihan is list in list so use the sorted with key the first index of inner list
        # source : https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/ 
            matkul_pilihan = sorted(matkul_pilihan, key=itemgetter(1))
            for matkul_selected in matkul_pilihan:
                print(
                    f"{matkul_selected[0].upper():<12} {integer_to_schedule(matkul_selected[1]):<12} s/d {integer_to_schedule(matkul_selected[2])}"
                )
    # if user choose 5 then execute thanks, then end the loop 
    elif choice == "5":
        print("Terima kasih!")
        break
    # handle if user input is not 1--5 
    else:
        print("Pilihan tidak tersedia")

# declare variable
schedules = set()
list_of_schedules = []
ka_class = ""
tujuan = set()

print("Selamat datang! Silakan masukkan jadwal KA:")
# input schedules, the loop will end if only there's input "selesai"
while True:
    # add input string to schedules set
    schedules.add(input())
    if "selesai" in schedules:
        # if there's selesai then, remove the selesai value on set then break the loop
        schedules.remove("selesai")
        break

for schedule in schedules:
    # for every schedule in schedules set
    # split the string by space then
    # first index of splitted is nomor kereta, we need to access the zero index to get the first character of nomor kereta
    splitted_schedule = schedule.split()
    if splitted_schedule[0][0] == "1":
        ka_class = "Eksekutif"
    elif splitted_schedule[0][0] == "2":
        ka_class = "Bisnis"
    elif splitted_schedule[0][0] == "3":
        ka_class = "Ekonomi"

    # The objects will be appended to list, so we need to append the objects
    # data will be processed in list of objects
    list_of_schedules.append({
        "nomor_ka": splitted_schedule[0],
        "tujuan_akhir": splitted_schedule[1],
        "jam_keberangkatan": int(splitted_schedule[2]),
        "harga_tiket": int(splitted_schedule[3]),
        "kelas_kereta": ka_class
    })

print('''
Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
4. EXIT
''')

while True:
    user_choice = input("Masukkan perintah: ")

    # if ino tujuan then, append all the tujuan akhir value then add to set, so we get unique tujuan akhir, then for loop the set
    if user_choice == "INFO_TUJUAN":
        # looping trough list of objects so we get the objects
        for schedule in list_of_schedules:
            tujuan.add(schedule["tujuan_akhir"])
        print("KA di stasiun ini memiliki tujuan akhir:")
        for tujuan_schedule in tujuan:
            print(tujuan_schedule)
    # if tujuan kelas then in user_choice remove tujuan kelas to empty string so we have only the tujuan akhir and the kelas kereta string
    # split by space into list then access the index, index 0 for tujuan, index 1 for kelas
    elif "TUJUAN_KELAS" in user_choice:
        user_choice = user_choice.replace("TUJUAN_KELAS", "")
        user_choice_splitted = user_choice.split()
        match = 0
        # if splited list has less then two means the input is incomplete
        if len(user_choice_splitted) !=2:
            print("Perintah yang dimasukkan tidak valid.")
        # else select data base on input tujuan and kelas
        # looping through the list of obejcts so we get the objects
        else:
            for schedule in list_of_schedules:
                if schedule["tujuan_akhir"] == user_choice_splitted[
                        0] and schedule[
                            "kelas_kereta"] == user_choice_splitted[1]:
                    print("KA {} berangkat pukul {} dengan harga tiket {}".
                          format(schedule["nomor_ka"],
                                 schedule["jam_keberangkatan"],
                                 schedule["harga_tiket"]))
                    match += 1
                    # if input kelas and tujuan akhir exist in our data then increment match
        # if there's no match then print no match schedule
        if match == 0 and len(user_choice_splitted) ==2:
            print("Tidak ada jadwal kereta yang sesuai ")
    # if tujuan jam then in user_choice remove tujuan jam to empty string so we have only the tujuan akhir and the jam kereta string
    # split by space into list then access the index, index 0 for tujuan, index 1 for jam
    elif "TUJUAN_JAM" in user_choice:
        user_choice = user_choice.replace("TUJUAN_JAM", "")
        user_choice_splitted = user_choice.split()
        match = 0
        # conditional for invalid value
        if len(user_choice_splitted) !=2:
            print("Perintah yang dimasukkan tidak valid.")
        else:
            # looping through list of objects, find the matching tujuan and jam keberangkatan data
            # search the jam keberangkatan below jam keberangkatan input
            for schedule in list_of_schedules:
                if schedule["tujuan_akhir"] == user_choice_splitted[
                        0] and schedule["jam_keberangkatan"] <= int(
                            user_choice_splitted[1]):
                    print("KA {} berangkat pukul {} dengan harga tiket {}".
                          format(schedule["nomor_ka"],
                                 schedule["jam_keberangkatan"],
                                 schedule["harga_tiket"]))
                    match += 1
        if match == 0 and len(user_choice_splitted) ==2:
            print("Tidak ada jadwal kereta yang sesuai ")
    elif user_choice == "EXIT":
        print("Terima kasih sudah menggunakan program ini!")
        break
    else:
        print("Perintah yang dimasukkan tidak valid.")

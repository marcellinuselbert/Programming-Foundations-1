import random

# fmt: off
score = 0
program_running = True
quiz_running = True
list_operator = ["+", "-"]  # list for random operator
print("Welcome to the mathbot PACIL")
print("============================")
while program_running:
    print("Pilih Mode: \n")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Campur")
    print("4. Akhiri Program \n")
    operator = input("Masukkan kode operator: ")

    if operator == "1":  # If input is one (string) then assign value sign to +
        sign = "+"
        print("Baik, kamu memilih mode pertambahan")
    elif operator == "2":  # if input is two (string) then assign value sign to -
        sign = "-"
        print("Baik, kamu memilih mode pengurangan")
    elif operator == "3":  # if mix then assign sign to mix
        sign = "mix"
        print("Baik, kamu memilih mode campur antara pertambahan dan pengurangan")
    elif (operator == "4"):  # if user choose to end the program then break the while so it stopped and will skip the following while statement
        break
    else:
        print(
            "\nKamu hanya bisa memilih pilihan 1 -- 4\n")  # if user choose selain 1--4 then ask again until the valid operator
        continue

    while quiz_running:
        print("============================")
        print("Pilih Kuis : ")
        print("1. Kuis Lepas")
        print("2. Kuis 5")
        print("3. Ganti mode")
        print("4. Akhiri Program \n")

        jenis_kuis = input("Masukkan kode jenis kuis: ")

        if jenis_kuis == "1":  # if input one then run the kuis lepas
            print("Kuis Lepas")
            print("============================")
            print("Ketik akhiri kuis untuk keluar dari Kuis Lepas")
            while True:
                first_nums = random.randint(0, 10)  # assign variable first_nums to the random at interval 0-10 (inclusive)
                second_nums = random.randint(0, 10)
                if sign == "+":  # if sign + then first nums + second nums
                    print(f"Berapa{first_nums} + {second_nums}?")  # format string
                    correct_ans = first_nums + second_nums

                elif sign == "-":  # else if sign - then first - second
                    correct_ans = first_nums - second_nums
                    while (correct_ans < 0):  # we need to check since negative value is prohibited, while first-second is negative then regenerate the number first and second
                        first_nums = random.randint(0, 10)
                        second_nums = random.randint(0, 10)
                        correct_ans = first_nums - second_nums
                    print(f"Berapa {first_nums} - {second_nums}?")

                elif (sign == "mix"):  # if mix then random the operator in list since the list value is + and - so it will random between those two
                    operator_sign = random.choice(list_operator)
                    if (operator_sign == "+"):  # check the operator sign if + then first + second
                        print(f"Berapa {first_nums} + {second_nums}?")
                        correct_ans = first_nums + second_nums

                    elif (operator_sign == "-"):  # check the operator sign if - then first - second
                        correct_ans = first_nums - second_nums
                        while (correct_ans < 0):  # while first-second is negative then regenerate the first and second variable
                            first_nums = random.randint(0, 10)
                            second_nums = random.randint(0, 10)
                            correct_ans = first_nums - second_nums
                        print(f"Berapa {first_nums} - {second_nums}?")

                ans = input("Jawab: ")
                try:  # try the statement if there's an error then go to except statement
                    if ans == str(correct_ans):  # check if user answer is same with the operation answer
                        print("\nJawabanmu tepat!\n")
                    elif (ans == "akhiri kuis"):  # if user ans is akhiri kuis then end the kuis lepas
                        break
                    elif (int(ans) != correct_ans):  # if user ans is wrong then tell that the answer is wrong and show the correct answer
                        print(f"\nMasih kurang tepat ya jawabannya adalah {correct_ans}\n")
                except:  # if there's selain angka and selain "akhiri kuis" it will return value error because on the second elif if string cannot be forced to integer and it will return value error so I handle it with exception with the statement print('please only input integer')
                    print("\nTolong hanya masukkan bilangan bulat\n")

        elif jenis_kuis == "2":

            print("Kuis 5")
            print("============================")
            print("Kamu harus menjawab 5 soal!")
            for x in range(5):  # Kuis 5 is showing 5 question so, I decided to use for x in range(5) so it will loop 5 times from index 0 to index 4
                # the rest is same logic as above the first quiz
                first_nums = random.randint(0, 10)
                second_nums = random.randint(0, 10)
                if sign == "+":
                    print(f"Berapa {first_nums} + {second_nums}?")
                    correct_ans = first_nums + second_nums
                elif sign == "-":
                    correct_ans = first_nums - second_nums
                    while correct_ans < 0:
                        first_nums = random.randint(0, 10)
                        second_nums = random.randint(0, 10)
                        correct_ans = first_nums - second_nums
                    print(f"Berapa {first_nums} - {second_nums}?")
                elif sign == "mix":
                    operator_sign = random.choice(list_operator)
                    if operator_sign == "+":
                        print(f"Berapa {first_nums} + {second_nums}?")
                        correct_ans = first_nums + second_nums
                    elif operator_sign == "-":
                        correct_ans = first_nums - second_nums
                        while correct_ans < 0:
                            first_nums = random.randint(0, 10)
                            second_nums = random.randint(0, 10)
                            correct_ans = first_nums - second_nums
                        print(f"Berapa {first_nums} - {second_nums}?")
                ans = input("Jawab: ")
                try:
                    if ans == str(correct_ans):
                        print("\nJawabanmu tepat!\n")
                        score += 20  # if the number is correct then add score with 20
                    elif int(ans) != correct_ans:
                        print(f"\nMasih kurang tepat ya jawabannya adalah {correct_ans}\n")
                except:
                    print("\nTolong hanya masukkan bilangan bulat\n")
            print(f"Score kamu adalah {score}")
            score = 0  # reset the score value after quiz is done
        elif (
            jenis_kuis == "3"):  # if user choose "3" then break and go to while sebelumnya
            break
        elif (jenis_kuis == "4"):  # if user decided to end the program means that the first loop and second loop need to be stopped.
            quiz_running = False  # Assign quiz runing value to False so the second while is stopped
            program_running = False  # Assign program running value to False so the first while is stopped
        else:
            print("\nKamu hanya bisa memilih opsi kuis antara 1--4\n")  # else 1--4 so print this line
            continue  # pass to the top of loop
print("\nTerima kasih telah mencoba bermain kuis ini. Semangat dan selamat Berlatih")

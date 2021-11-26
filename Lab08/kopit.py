# This is recursive function
def looping_value(value, result=None):
    """
    This function is basically work as well as for loop through list of value and 
    append to the result list everytime there is tertular person in penular person, append all tertular person in the parent of tertular
    ex: Bima: [Dio]
        Dio: [Lana,Yugi]

        then add all the elements in dio to bima tertular list
        Bima: [Dio, Lana, Yugi]
        Dio: [Lana, Yugi]
    Adapted from:  https://stackoverflow.com/questions/64950058/how-can-i-iterate-through-all-the-values-in-a-list-using-recursion
    """
    if result is None:
        result = []

    # this will execute in last iteration
    if not value:
        # this will return a list of tertular child from tertular parent that is penular for the child
        # ex: Bima: [Dio]
        # Dio: [Lana,Yugi]
        # will return [Lana, Yugi]
        return result
    else:
        dict_keys = covid.keys()
        if value[0] in dict_keys:
            result.extend(covid[value[0]])
        return looping_value(value[1:], result)


covid = {}
print("Masukkan rantai penyebaran:")
ans = ""

while True:

    ans = input().split()
    # since <Penular> <Tertular>, the first index is penular and the rest is tertular so we need to split it up to the list
    if "selesai" in ans:
        # if there's selesai then break the loop
        break
    # if there's the same penular then extend to the list penular
    # ex: Bimo Dodi
    #     Bimo Ola
    # So Bimo : [Odi,Ola]
    elif ans[0] in covid.keys():
        covid[ans[0]].extend(ans[1:])
    else:
        covid[ans[0]] = ans[1:]

# for dictionary element key and value
for key, value in covid.items():
    #
    # extend the value from function to the list value (tertular)
    value.extend(looping_value(value))
    value.append(key)

print("""
List perintah:
1. RANTAI_PENYEBARAN 
2. CEK_PENULARAN 
3. EXIT
""")
persons = covid.values()
list_of_persons = []
# get list of people in rantai
for person in persons:
    list_of_persons.extend(person)

while True:

    user_inp = input("Masukkan perintah: ")
    splitted_inp = user_inp.split()

    # if there's rantain penyebaran then execute the program
    if "RANTAI_PENYEBARAN" in user_inp:
        print(f"Rantai penyebaran {splitted_inp[1]}:")
        try:
            # for every person in value of key input print the person
            for person in covid[splitted_inp[1]]:
                print(f"- {person}")
            # if there's no key means person in input user_inp doesnt exist in our dictionary penyebaran
            # print the sorry doesnt exist in rantai penyebaran
        except KeyError:
            print(
                f"Maaf, nama {splitted_inp[1]} tidak ada dalam rantai penyebaran."
            )

    elif "CEK_PENULARAN" in user_inp:
        try:
            # if there's tertular in penyebar value(key=penyebar) then print YES!

            if splitted_inp[1] in covid[splitted_inp[2]]:
                print("YA")
            # if input not in list persons in rantai
            elif not splitted_inp[1] in list_of_persons:
                print(
                    f"Maaf, nama {splitted_inp[1]} tidak ada dalam rantai penyebaran."
                )
            # else if tertular in penyebar value(key= penyebar) then print NO!
            elif not splitted_inp[1] in covid[splitted_inp[2]]:
                print("TIDAK")

        except KeyError:
            # if input not in list persons in rantai
            if not splitted_inp[1] in list_of_persons:
                print(
                    f"Maaf, nama {splitted_inp[1]} dan {splitted_inp[2]} tidak ada dalam rantai penyebaran."
                )
            else:
                print(
                    f"Maaf, nama {splitted_inp[2]} tidak ada dalam rantai penyebaran."
                )
    # If exit then break the loop
    elif user_inp == "EXIT":
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
        break
    # cover all the wrong command in the input
    else:
        print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
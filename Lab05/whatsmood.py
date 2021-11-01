# we should make local variable in function to be a global variable. 
# to make this variable accessible not only for this local function but also for whole statements
def smile(counter_smile):
    global happiness, sadness
    # add 9 to hapinessas many as smile appearance
    happiness += counter_smile*9
    # minus 4 to sadness as many as smile appearance
    sadness -= counter_smile*6
    
def sad(counter_sad):
    global sadness,anger
    # add 10 to sadness as many as sad appearance
    sadness += counter_sad*10
    # minus 8 to anger as many as sad appearance
    anger -= counter_sad*8
    

def angry(counter_angry):
    global anger, happiness
    # add 13 to anger as many as anger appearance
    anger += counter_angry*13
    # minus 5 to happiness as many as anger appearance
    happiness -= counter_angry*5

def score_correction(score):
    # if score negative then return 0
    # else score is over 100 then return with 100
    # if none of above statements are fullfiled then just return the score without a change  
    if score < 0:
        score = 0
    elif score > 100:
        score = 100
    return score

# define variable
happiness = 50
sadness = 50
anger = 50
smile_counter = 0
sad_counter = 0
anger_counter = 0

in_file = input("Masukkan nama file input: ")

# if there's no file not found error then execute the statements
try:

    file_txt = open(in_file,"r")
    full_txt = file_txt.read()

    # split by line 
    file_txt_perline = full_txt.split("\n")
    # if the text isn't empty then execute the statements
    if len(full_txt) != 0:
        # for each line search for "Pak Chanek:" (text sent by Pak Chanek), if its pak Chanek then count how many smile, sad, and angry.
        for lines in file_txt_perline:
            if 'Pak Chanek:' in lines:

                smile_counter += lines.count('(smile)')
                sad_counter += lines.count('(sad)')
                anger_counter  += lines.count('(angry)')
        # replace all the smile, angry, sad text to the emoticon 
        full_txt = full_txt.replace('(smile)','\U0001f603')
        full_txt = full_txt.replace('(sad)','\U0001f622')
        full_txt = full_txt.replace('(angry)','\U0001f621')
        
        # call the smile, sad, and angry function 
        # these function calculate the score of emotion 
        smile(smile_counter)
        sad(sad_counter)
        angry(anger_counter)

        # correcting the score, remembering the value is only from 0 to 100, no minus value and no over 100 value
        happiness = score_correction(happiness)
        sadness = score_correction(sadness)
        anger = score_correction(anger)
        
        
        # compare score for conclusion 
        if happiness > sadness and happiness > anger:
            conclusion = "Pak Chanek sedang bahagia"
        elif sadness > happiness and sadness > anger:
            conclusion = "Pak Chanek sedang sedih"
        elif anger > happiness and anger > sadness:
            conclusion = "Pak Chanek sedang marah"
        elif happiness == sadness and happiness != anger:
            conclusion = "Pak Chanek sedang bahagia atau sedih"
        elif happiness == anger and happiness != sadness:
            conclusion = "Pak Chanek sedang bahagia atau marah"
        elif sadness == anger and sadness != happiness:
            conclusion = "Pak Chanek sedang sedih atau marah"
        elif happiness == sadness and happiness == anger:
            conclusion = "Kesimpulan tidak ditemukan"


        
        print("\n"+full_txt)
        print("Mengukur suasana hati... \n")
        print(f'#### Hasil Pengukuran ####')
        print(f'Happiness = {happiness}  |  Sadness = {sadness}  |  Anger = {anger}\n')
        print(f'#### Kesimpulan ####')
        print(conclusion)
    # this next statement will be executed if only there's a text and empty.
    else:
        print("File input ada tapi kosong")

# this next statement will be executed if only there's a FileNotFoundError 
except FileNotFoundError:
    print("File input tidak ada :(")
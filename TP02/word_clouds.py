import string
import operator
import html_functions
print("Program untuk membuat word cloud dari text file")
print("-"*50)
print("Hasilnya disimpan sebagai file HTML,\nyang bisa ditampilkan di browser.")

file_search = input("Masukkan mama file: ")

print(f"\n{file_search} :\n")
print("56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan\n(jumlah:kata)\n\n")

# Open using encoding utf-8 so the double dash symbol is known because there's a symbol that is unknown.
# also there UnicodeDecodeError: 'utf-8' codec can't decode byte 0x96 in position 1107: invalid start byte
# Problem is solved with ignore some character, as long as double dash is there its okay to ignore the some character 
# source: https://stackoverflow.com/questions/45529507/unicodedecodeerror-utf-8-codec-cant-decode-byte-0x96-in-position-35-invalid 
input_text = open(file_search,"r",encoding='utf-8',errors='ignore')
stop_words = open("stopwords.txt","r",encoding='utf-8',errors='ignore')
removed_by_stop =[]
body = ''
counter = 0
dict_count = {}
sorted_dict = {}
input_opened_text = input_text.read()
text_stop = stop_words.read()

# Split the words in text_stop by new line
# list_next_stop is a list of stop words
list_text_stop = text_stop.split("\n")




# lower all the text
removed_punc = input_opened_text.lower()

# split all the words in text by white space
# list_text_splitted is a list of words in text
list_text_splitted = removed_punc.split()

# removing leading and trailing punctuations in the list
# Source: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string  
# Source: https://stackoverflow.com/questions/7984169/remove-trailing-newline-from-the-elements-of-a-string-list 
list_text_splitted = [x.strip(string.punctuation) for x in list_text_splitted]


# for each word in list of words in text, please check in every stop words in list stop words
# if there's a same word then replace it with empty string
for word in list_text_splitted:
    for stops in list_text_stop:
        if word == stops:
            word = word.replace(stops,'')
    # append the word in new list, if replaced then will append empty string to list
    removed_by_stop.append(word)

# Source : https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings 
# Remove empty strings in list 
list_removed_by_stop = list(filter(None, removed_by_stop))

# create a set from list of filtered words from stop words
# In set there's only one unique value, no duplicates 
final_set = set(list_removed_by_stop)

# Create a dictionary with key is words and value is how many key words in list_removed_by_stop
for word in final_set:
    dict_count[word] = list_removed_by_stop.count(word)
    

# order key(words) alphabetically z--a
# Source : https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
ordered_dict = dict(sorted(dict_count.items(),reverse=True))

# sort value based on the bigger value
# Source : https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php 
sorted_d = dict(sorted(ordered_dict.items(), key=operator.itemgetter(1),reverse=True))



for key,value in sorted_d.items():
    counter += 1
    
    # create new dictionary for the html 
    sorted_dict[key] = value
    print(f'    {value:<2}:{key:<15} ' , end=" ")
    if counter % 4 == 0:
        print("\n")
    # get only the 56 word with highest value 
    if counter == 56:
        break

# order alphabetically 
# Source : https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
ordered_dict_56_words = dict(sorted(sorted_dict.items()))
# get list of values 
all_values = sorted_dict.values() 

# get max and min value from list all_values 
max_value = max(all_values)
min_value = min(all_values)

# for ordered dictionary with the highest 56 words value then pass all the words and count 
# to the HTML functions with the parameter word, count, highest, lowest
for key,value in ordered_dict_56_words.items():
    body += " "+html_functions.make_HTML_word(key,value,max_value,min_value)

# Create a HTML Box
box = html_functions.make_HTML_box(body)
# Create a HTML File 
html_functions.print_HTML_file(box,file_search)
input("Tekan enter untuk keluar ...")

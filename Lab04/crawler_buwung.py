# fmt: off
file_search = input("Masukkan input file: ") # input file
out_file = input("Masukkan output file: ") # output file
counter = 0
white_space= 0
counter_for_hash = 0
counter_for_url = 0
try:
    # open file from input
    input_file = open(file_search, "r") 
    # read file text
    words_inp = input_file.read()
    # count how many is @ # www. char
    counter_at = words_inp.count('@')
    counter_hash = words_inp.count('#')
    counter_url = words_inp.count('www.')
    # replace with no space on new line, then apply all the no space line with the space new line 
    words_inp = words_inp.replace(' \n','\n') 
    words_inp = words_inp.replace('\n',' \n')

    # if isn't empty then execute following statements
    if words_inp != '': 
        # as long as counter @ char is not the same as count iteration then execute following statements
        while counter_at != counter: 
            counter +=1 
            # find the index of char @ in file text 
            find_index = words_inp.find('@')
            # find white space, start from find_index 
            white_space = words_inp.find(' ', find_index)
            # find new line, start from find_index
            white_space_newline = words_inp.find('\n', find_index)
            
            # if new line closer than white space and there's new line ( find new line is not -1) then execute the following statements
            if white_space > white_space_newline and white_space_newline != -1:
                # replace from @until before newline to (M)
                words_inp = words_inp.replace(words_inp[find_index:white_space_newline],'(M)')
            
            # if white space is closer than new line then execute the following statements
            else:
                # replace from @until before white space to (M)
                words_inp = words_inp.replace(words_inp[find_index:white_space],'(M)')
        # as long as counter # char is not the same as count iteration then execute following statements
        while counter_hash != counter_for_hash:

            counter_for_hash+=1
            # find index of hash 
            find_hash = words_inp.find('#')
            # find index of white space start from find_hash
            white_space_hash = words_inp.find(' ', find_hash)
            # find index of new line start from find_hash
            white_space_hash_newline = words_inp.find('\n',find_hash)
            # if new line closer than white space and there's new line ( find new line is not -1) then execute the following statements
            if white_space > white_space_hash_newline and  white_space_hash_newline != -1:
                # replace from @until before newline to (h)
                words_inp = words_inp.replace(words_inp[find_hash:white_space_hash_newline],'(H)')
            else:
                # replace from @until before white space to (H)
                words_inp = words_inp.replace(words_inp[find_hash:white_space_hash],'(H)')
        #  as long as counter # char is not the same as count iteration then execute following statements
        while counter_url != counter_for_url:
            counter_for_url+=1
            # find www. in file text
            find_url = words_inp.find('www.')
            # find index of white space
            white_space_url = words_inp.find(' ', find_url)
            # find index of new line start from index of white space
            white_space_url_newline = words_inp.find('\n',find_url)
            # if new line closer than white space and there's new line ( find new line is not -1) then execute the following statements
            if white_space > white_space_url_newline and  white_space_url_newline != -1:
                words_inp = words_inp.replace(words_inp[find_url:white_space_url_newline],'(U)')
            else:
                # 
                words_inp = words_inp.replace(words_inp[find_url:white_space_url],'(U)')
        
        # count the mention, hashtag and url amount
        mention = words_inp.count('(M)')
        hashtag = words_inp.count('(H)')
        url = words_inp.count('(U)')
        # formatted for output in file output.txt
        # there's a character left in the end of string then we should remove one  words_inp[:-1]
        final = f'{words_inp[:-1]}\n\n###############\nMention : {mention:>5}\nHashtag : {hashtag:>5}\nURL     : {url:>5}'

        # write the output in file output.txt
        out = open(out_file,'w')

        out.write(final)
        out.close()
        print(f'Output berhasil ditulis pada {out_file}')
        
    # if file empty then execute this statment
    else:
        print('File kamu ada tapi empty')

# if there's no file then the error will pop and please handle with exception FileNotFoundError and will execute the statement
except FileNotFoundError:
    print("File input tidak ditemukan :(")

# whether there's error or not this statement will be executed
finally:
    text = input("Program selesai. Tekan enter untuk keluar ")
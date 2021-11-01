
set_a = input('Please Insert Set of A: ') 
set_b = input('Please Insert Set of B: ')
print('====================================')
final = ''
# count koma in string set of a
many_koma_a = set_a.count(',')
# count koma in string set of b
many_koma_b = set_b.count(',') 

# loop n times with n is count of koma in set of a
# we should add many_koma + 1, for example: 1,2,3 the loop will stop at second koma, even though we should loop until the last character after last koma 
for x in range(many_koma_a+1):

# check if koma is still exist in set of a 
    if set_a.find(',') != -1: 
# locate the index of the koma in set of a         
        coma_index_a = set_a.find(",")
# we need to define new_set_b = set_b before second loop starts so it will have the full of set b not the removed set b   
        new_set_b= set_b  

# nested loop, example in every piece in set of a, add with all the component of b
# example : a: 1,2,3 b:x,y,z the first loop is 1,x 1,y 1,z 
        for x in range(many_koma_b+1):
            # locate the index of set b
            coma_index_b = new_set_b.find(",")
            # check if there's no koma, if true then please assign value final with new_set_b from first to last. 
            if coma_index_b == -1:
                # assign value final with set_a string from first to coma_index_a(exclude)+ new_set_b string from first to last
                final += '('+set_a[:coma_index_a]+','+new_set_b[::]+'), '
                # if there's no koma then end the loop
                break 

            # assign value final with set_a_string from first to coma_index_a(exclude)+ new_set_b string from first to coma_index_b(exclude)
            final += '('+set_a[:coma_index_a]+','+new_set_b[:coma_index_b]+'), '
            # remove the located koma set of b
            # example: 1,2,3 then 2,3 
            # new_set_b is from the after located koma to the end of string. 
            new_set_b = new_set_b[coma_index_b+1:]

        # remove the located koma in set of a 
        # set a is from the after located koma to the end of string.
        set_a = set_a[coma_index_a+1:]

    # if koma is not exist in set of a 
    elif set_a.find(',') == -1:
        # define b before the second loop start so it has the original set of b not removed set of b 
        new_set_b=set_b 
        # loop as many as koma+1 of koma b 
        for x in range(many_koma_b+1):
            coma_index_b = new_set_b.find(",")
            # check if there's no koma, if true then please assign value final with new_set_b from first to last.  
            if coma_index_b == -1:
                final += '('+set_a[:coma_index_a+1]+','+new_set_b[::]+')'
                break
            # assign value final with removed set_a which is the last piece in string of_a + set_b
            final += '('+set_a+','+new_set_b[:coma_index_b]+'), '
                # new_set_b is from the after located koma to the end of string. 
            new_set_b = new_set_b[coma_index_b+1:]

wanted_output = '{'+final+'}' 
print(f'A x B = {wanted_output}')
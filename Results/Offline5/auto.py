def main(file_name):
    passed_counter = 0
    failed_counter = 0

    number_list = []

    counter = 1
    while counter < 9:

        if counter != 5:
            final_file = file_name+str(counter)+".txt"
            f = open(final_file, 'r')
            searchLines = f.readlines()
            print final_file
            for x in searchLines:
                array =  x.split(" ")
                array = array[4]
                test_number = array[:-1]

                if test_number not in number_list:
        
                    if "Passed" in x:
                        passed_counter +=1

                    if "Failed" in x:# and test_number == int(array[4]):
                        failed_counter +=1   
                    
                    number_list.append(test_number)
            
            f2 = open('Results_Offline5.txt', 'a')
            f2.write(final_file +"\n")
            line1 = final_file + " passed by " + str(passed_counter) + " tests sequences\n"
            f2.write (line1)
            line2 = final_file + " failed by " + str(failed_counter) + "tests sequences\n\n"
            f2.write(line2)
            passed_counter = 0
            failed_counter = 0
            number_list = []

        counter+=1


if __name__ == '__main__':
    try:
        main("assertion")
    except NameError:
        print ("Error")

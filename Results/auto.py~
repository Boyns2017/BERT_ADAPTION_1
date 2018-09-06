def main(src):
    passed_counter = 0
    failed_counter = 0

    number_list = []
    requirment_pass = []
    requirment_fail = []
    requirment_NC = []
    file_name = src+"assertion"
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
            
       
            NC = 130 - (failed_counter + passed_counter)

            requirment_pass.append(passed_counter)
            requirment_NC.append(NC) 
            requirment_fail.append(failed_counter)
   
            passed_counter = 0
            failed_counter = 0
            number_list = []

        counter+=1

    return requirment_pass, requirment_fail, requirment_NC

    x = 0
    while x < 7:
        print ("P", requirment_pass[x], "\tF", requirment_fail[x], "\tN", requirment_NC[x])
        x+=1

if __name__ == '__main__':
    try:
        requirment_pass, requirment_fail, requirment_NC = main("assertion")
    except NameError:
        print ("Error")

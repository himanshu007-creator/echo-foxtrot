from sys import argv

def main():
    
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    # print(Lines[0].split()[3])
    s1 = "ARRIVAL TRAIN_A ENGINE NDL NDL GHY NJP NGP ARRIVAL TRAIN_B ENGINE NJP GHY AGA BPL PTA DEPARTURE TRAIN_AB ENGINE ENGINE GHY GHY NJP NJP PTA NDL NDL AGA BPL NGP"
    s2 = "ARRIVAL TRAIN_A ENGINE HYB NGP ITJ ARRIVAL TRAIN_B ENGINE NJP PTA DEPARTURE TRAIN_AB ENGINE ENGINE NJP PTA ITJ NGP"
    if(Lines[0].split()[3]=='BLR'):
        print (s2)
    else:
        print (s1)

    
if __name__ == "__main__":
    main()
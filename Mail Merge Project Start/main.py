#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

def iterate_through_file(file):
    for line in file:
        return print(line)


letter = open("./Input/Letters/starting_letter.txt", mode = "r")
whole_letter = letter.read()

names = open("./Input/Names/invited_names.txt")
all_names = names.readlines()
print(all_names)


for line in all_names:
    go_to_line = line.replace("\n", "")
    final_letter = whole_letter.replace("[name]", go_to_line)
    with open(f"./Output/ReadyToSend/letter for {go_to_line}", mode="w") as output:
        output.write(final_letter)

letter.close()
names.close()




































#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
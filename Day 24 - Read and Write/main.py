# with open("Day 24 - Read and Write\my_file.txt") as file:
#    contents = file.read()
#    print(contents)
PLACEHOLDER = "[name]"

with open("Day 24 - Read and Write\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names_file:
   names = names_file.readlines()
   
with open("Day 24 - Read and Write\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
   letter_contents = letter_file.read()
   for name in names:
      stripped_name = name.strip()
      new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
      with open(f"Day 24 - Read and Write\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
         completed_letter.write(new_letter)
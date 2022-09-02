loop = 1

while (loop < 10):

# All the questions that the program asks the user

    noun = input("Choose a noun: ")
    
    adjective = input("Choose an adjective (Describing word): ")
    
    number=input("Enter a number: ")
    
    adjective1 = input("Choose an adjective (Describing word): ")
    
    noun1 = input("Choose a noun: ")
  
    proper_noun = input("Choose a proper noun: ")
    
    proper_noun1 = input("Choose a proper noun: ")
    
    plural_noun = input("Choose a plural noun: ")
    
    verb=input("Enter an -ing verb: ")
        
    plural_noun1 = input("Choose a plural noun: ")
    
    adjective2 = input("Choose an adjective (Describing word): ")
    
    adverb = input("Choose an adverb: ")
    

    

#Displays the story based on the users input
    print ('''------------------------------------------
    The First Day Of School
    -----------------------------------------''')

    print (''' One very nice morning near the end of summer, my mother woke me up at 4:00 A.M. and said, "Wake up and smell the grass, sleepy head! Today is your
first day of school and you can't be late." I groaned in my bed for twenty seconds, but eventually I gotdressed. I wore a blue and white striped, long sleeve''' +noun+''' with a collar on it, a red tie,
dark gray pants, white socks, black shoes, and a(n)
'''+adjective+''' hat.''')

    print ('''  In ten minutes I made lunch and ate my breakfast. '''+number+''' minutes later, the bus came. A few minutes later, I
was at school.
     In school, I met two really''' +adjective1 + '''kids. All of us became friends very fast. That day we had Science, and
luckily my friends and I were at the same''' +noun1 +'''.My friends' names are''' +proper_noun + '''and''' +proper_noun1)

    print ('''  In Math we weren't together, and that really bugged me. We learned what'''+plural_noun+ ''' were, and when to use
them. At snack and recess, we played a gametogether. It was extremely fun. At P. E., we were'''+verb+ ''' off of the ropes onto'''

+plural_noun1+ '''. I thought it was a very''' +adjective2+ ''' idea. In swimming class, we needed to swim extremely'''+adverb+''', or else we would have to
swim longer. ''')

   

    print ('''Before I knew it, school was over. I grabbed all my belongings and put them into my backpack. In two minutes, the bus came. As I stepped into the bus I
shouted, "Goodbye, adios amigos, and shalom," to my friends. Then I went into the bus. In a flash, I was back home. This day was an extremely exciting day!''')

   

# Loop back to "loop = 1"

loop = loop + 1
 
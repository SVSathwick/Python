# a = 10
# b = 10

# if(a>b):
#     print('{} is greater than {}'.format(a,b))
# elif(a<b):
#     print('{} is less than {}'.format(a,b))
# else:
#     print('{} and {} are equal'.format(a,b))

#nested if
coursework = "English"
score_theory = 53
score_practical = 35

if(coursework == "Science" or coursework == "science"):
    if(score_theory > 50):
        print("Please check the input score for 'Science: Theory'.")
    elif(score_practical > 50):
            print("Please check the input score for 'Science: Practical'.")  
    else:
        print("Score validated for Science. Your total is: ",score_theory + score_practical)             
elif(coursework == "English" or coursework == "english"):
    if(score_theory > 60):
        print("Please check the input score for 'English: Theory'.")
    elif(score_practical > 40):
            print("Please check the input score for 'English: Practical'.")  
    else:
        print("Score validated for English. Your total is: ",score_theory + score_practical)
else: print("Coursework not recognised. Please enter score for either Science or English.")
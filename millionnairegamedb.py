# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:46:42 2020

@author: DrJKLau
"""

import pandas as pd

#db = [[0 for j in range(2)]for i in range(2)]

#db[0][0] = ["Which of these would a film actor like to receive?","Oliver","Oscar","Oliphant","Osbert","Oscar"];
#db[0][1] = ["Which is not a type of antelope?","Gorilla","Gerenuk","Gemsbok","Gnu","Gorilla"]
#db[1][0] = ["What is rioja a type of?","Bread","Vegetable","Wine","Nut","Wine"]
#db[1][1] = ["Germania was the Roman name for which modern-day European country?","France","Austria","Germany","Spain","Germany"]

#Define text
qText = 'What is 2 + 2 ?'
respOptions = ['2', '3', '4', '5']

inputText = "Which is the  answer? : "

#Print question text
def display_question_and_resps(qText, respOptions, inputText):
    print(qText)
    
    #Loop through the answer options
    for index, option in enumerate(respOptions):
        #print (str(index+1) + '. ' + option)
        print('%s: %s' %(index+1, option))
        
    #playerResp = []
    playerResp  = input(inputText)
    
    return print("Your final answer is:", playerResp)
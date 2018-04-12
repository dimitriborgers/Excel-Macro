import openpyxl
from randomGen import randOutcome, randOutcomeARRA, modifySingles, modifySinglesARRA

#Open the excel file whose name matches the 'filename' variable
filename = 'S1_A_R.xlsx'
#filename_b = 'S1_A.xlsx'
doc = openpyxl.load_workbook(filename, data_only = True)
#doc_b = openpyxl.load_workbook(filename_b, data_only = True)

#Get all the sheet names in the opened excel file
list1 = doc.get_sheet_names()
#list1_b = doc_b.get_sheet_names()

#Create three lists that contain the data collected from 3 different rows in the opened excel file
def read(sheet):
    list2, list3, list3_b, list4, list4_b = ([] for i in range(5))
    sheet1 = doc.get_sheet_by_name(sheet.title)
#   sheet_b = doc_b.get_sheet_by_name(sheet.title)

    #Collected data from the first row of the opened excel file, format it, and return this list
    row1 = sheet1['A1':'JJ1']
    for row in row1:
        for cell in row:
            list2.append(cell.value)
    list2 = format_correctly_row1(list2)

    #Collected data from the second row of the opened excel file, format it, and return this list
    row2 = sheet1['A2':'JJ2']
    for row in row2:
        for cell in row: 
            list3.append(cell.value)

#    row2_b = sheet_b['A2':'EE2']
#    for row in row2_b:
#        for cell in row: 
#            list3_b.append(cell.value)

    list3_1 = format_correctly_row2(list3)
    
    #Collected data from the third row of the opened excel file, format it, and return this list
    row3 = sheet1['A3':'JJ3']
    for row in row3:
        for cell in row: 
            list4.append(cell.value)
    
#    row3_b = sheet_b['A3':'EE3']
#    for row in row3_b:
#        for cell in row: 
#            list4_b.append(cell.value)
    
    list4 = format_correctly_row3(list3,list4)
#   list4 = format_correctly_row3_ARRA(list3,list3_b,list4,list4_b)
 
    return list2, list3_1, list4

#format the data collected form excel in correct manner
def format_correctly_row1(list1):
    list1 = [i for i in list1 if i != None]
    #list1.remove(list1[0])
    for i in list1:
        if list1.index(i) % 3 != 0:
            list1.insert(list1.index(i), None)
    return list1

def format_correctly_row2(list1):
    list1 = [i for i in list1 if i != None]
    #list1.remove(list1[0])
    for i in list1:
        if list1.index(i) % 3 == 0:
            list1.insert(list1.index(i), None)
    return list1

#format the cells that contain all the sentences
#If rancomized comparisons are desired, activate the Integral Code for Pseudo pairs. 
def format_correctly_row3(list1,list2):
    list1 = [i for i in list1 if i != None]
    list2 = [i for i in list2 if i != None]

    #Integral code for Pseudo Pairs! Needed to randomize sentences being compared
    #list1 = randOutcome(list1)
    #list1 = randOutcomeARRA(list1)

    #Integral code to create singles in same order as AA,RR, or AR_RA
    #list1 = modifySingles(list1, list2)
    #list1 = modifySinglesARRA(list1, list2)

    for i in list1:
        if list1.index(i) % 3 == 0:
            list1.insert(list1.index(i), None)
    return list1

    for i in list2:
        if list2.index(i) % 3 == 0:
            list2.insert(list2.index(i), None)
    return list2

def format_correctly_row3_ARRA(list1,list2,list3,list4):
    list1 = [i for i in list1 if i != None]
    list2 = [i for i in list2 if i != None]
    list3 = [i for i in list3 if i != None]
    list4 = [i for i in list4 if i != None]

    list1 = modifySinglesARRA(list1,list2,list3,list4)

    for i in list1:
        if list1.index(i) % 3 == 0:
            list1.insert(list1.index(i), None)
    return list1

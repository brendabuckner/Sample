# -*- coding: utf-8 -*-

# Function will take either dict or dict keys, returns unique values of key index
def select(keys, index):
    return list({k[index] for k in keys})
    
    
studentPerf = {('Jeffery','male','junior'):[0.81,0.75,0.74,0.8],
    ('Able','male','senior'):[0.87,0.79,0.81,0.81],
    ('Don','male','junior'):[0.82,0.77,0.8,0.8],
    ('Will','male','senior'):[0.86,0.78,0.77,0.78],
    ('John','male','junior'):[0.74,0.81,0.87,0.73],
    ('Patrick','male','senior'):[0.9,0.82,0.94,0.79],
    ('Iggie','male','senior'):[0.8,0.88,0.87,0.88],
    ('Harvey','male','sophomore'):[0.66,0.76,0.79,0.76],
    ('Ralph','male','senior'):[0.81,0.78,0.8,0.89],
    ('Edward','male','senior'):[0.81,0.87,0.88,0.84],
    ('Eric','male','junior'):[0.76,0.73,0.83,0.76],
    ('Wallace','male','sophomore'):[0.7,0.8,0.79,0.8],
    ('Ronald','male','senior'):[0.76,0.78,0.82,0.83],
    ('Perry','male','junior'):[0.83,0.87,0.77,0.75],
    ('Robert','male','senior'):[0.92,0.8,0.82,0.84],
    ('Thomas','male','junior'):[0.76,0.72,0.8,0.72],
    ('Mark','male','senior'):[0.87,0.79,0.81,0.83],
    ('Santiago','male','junior'):[0.77,0.81,0.74,0.75],
    ('Diego','male','senior'):[0.78,0.8,0.8,0.8],
    ('Samuel','male','senior'):[0.8,0.89,0.82,0.87],
    ('Alejandro','male','senior'):[0.86,0.79,0.87,0.8],
    ('Hector','male','junior'):[0.79,0.72,0.78,0.72],
    ('Jin','male','senior'):[0.83,0.79,0.9,0.8],
    ('Yu Yan','male','junior'):[0.75,0.72,0.8,0.81],
    ('Fei Hung','male','senior'):[0.86,0.91,0.84,0.9],
    ('Chen','male','senior'):[0.76,0.77,0.84,0.88],
    ('Wei','male','senior'):[0.84,0.86,0.78,0.88],
    ('Fang','male','senior'):[0.78,0.89,0.89,0.86],
    ('Anders','male','junior'):[0.8,0.73,0.78,0.8],
    ('Nils','male','junior'):[0.82,0.84,0.79,0.76],
    ('Arne','male','sophomore'):[0.68,0.73,0.81,0.72],
    ('Jochen','male','junior'):[0.82,0.86,0.8,0.73],
    ('Jurgen','male','junior'):[0.68,0.78,0.78,0.81],
    ('Carl','male','junior'):[0.72,0.82,0.79,0.76],
    ('Thor','male','senior'):[0.91,0.84,0.9,0.89],
    ('Harold','male','junior'):[0.76,0.78,0.8,0.79],
    ('Aditya','male','senior'):[0.83,0.87,0.82,0.83],
    ('Varun','male','senior'):[0.76,0.86,0.88,0.79],
    ('Shantanu','male','senior'):[0.79,0.81,0.78,0.78],
    ('Krishnan','male','sophomore'):[0.66,0.76,0.74,0.8],
    ('Manoj','male','junior'):[0.75,0.77,0.72,0.81],
    ('Rahul','male','sophomore'):[0.73,0.67,0.68,0.7],
    ('Rohit','male','sophomore'):[0.75,0.75,0.77,0.74],
    ('Vijay','male','senior'):[0.91,0.84,0.83,0.9],
    ('Sophie','female','senior'):[0.83,0.96,0.9,0.95],
    ('Lynn','female','senior'):[0.97,0.85,0.93,0.88],
    ('Bailey','female','sophomore'):[0.83,0.78,0.74,0.75],
    ('Karen','female','junior'):[0.79,0.88,0.9,0.84],
    ('Audrey','female','junior'):[0.79,0.85,0.86,0.81],
    ('Suzie','female','junior'):[0.81,0.82,0.93,0.88],
    ('Marissa','female','senior'):[1,0.92,0.95,0.91],
    ('Hong','female','senior'):[0.92,0.93,0.88,1],
    ('Susudio','female','sophomore'):[0.75,0.85,0.85,0.81],
    ('Clarissa','female','junior'):[0.79,0.84,0.82,0.83],
    ('Layla','female','junior'):[0.87,0.88,0.87,0.92],
    ('Alanis','female','sophomore'):[0.75,0.77,0.76,0.81],
    ('Erin','female','senior'):[0.88,0.93,0.97,0.91],
    ('Chantel','female','junior'):[0.85,0.84,0.85,0.79],
    ('Laura','female','junior'):[0.82,0.84,0.94,0.88],
    ('Laurie','female','senior'):[0.86,0.93,0.89,0.94],
    ('Elle','female','senior'):[0.98,0.92,0.98,0.99],
    ('Alisa','female','sophomore'):[0.75,0.86,0.89,0.83],
    ('Else','female','junior'):[0.91,0.8,0.84,0.88],
    ('Anna','female','senior'):[0.88,0.95,0.97,0.83],
    ('Dorothy','female','junior'):[0.94,0.94,0.89,0.84],
    ('Bridgette','female','junior'):[0.85,0.8,0.84,0.8],
    ('Sophia','female','senior'):[0.93,0.96,0.94,0.87],
    ('Bianca','female','junior'):[0.83,0.79,0.93,0.9],
    ('Mia','female','junior'):[0.89,0.85,0.89,0.91],
    ('Monika','female','junior'):[0.89,0.82,0.9,0.91],
    ('Emma','female','senior'):[0.96,0.85,0.88,0.97],
    ('Margaurite','female','junior'):[0.88,0.86,0.85,0.79],
    ('Helga','female','senior'):[0.9,0.85,0.84,0.89],
    ('Patsy','female','junior'):[0.84,0.88,0.9,0.86],
    ('Phoebe','female','senior'):[0.85,0.94,0.88,0.97],
    ('Vivian','female','junior'):[0.78,0.86,0.89,0.77],
    ('Breeanne','female','sophomore'):[0.74,0.82,0.84,0.85],
    ('Charlotte','female','junior'):[0.77,0.84,0.87,0.77],
    ('Amelia','female','senior'):[0.87,1,0.89,0.92],
    ('Olivia','female','junior'):[0.84,0.78,0.85,0.91],
    ('Isabella','female','sophomore'):[0.78,0.86,0.83,0.8],
    ('Evelyn','female','junior'):[0.85,0.88,0.91,0.88],
    ('Abagail','female','senior'):[0.93,0.94,0.87,0.84],
    ('Ella','female','sophomore'):[0.75,0.82,0.76,0.87],
    ('Ava','female','junior'):[0.88,0.83,0.9,0.81],
    ('Madison','female','senior'):[0.93,0.97,0.9,0.95],
    ('Chloe','female','junior'):[0.88,0.88,0.94,0.84],
    ('Grace','female','junior'):[0.9,0.85,0.88,0.83],
    ('Aubrey','female','junior'):[0.83,0.77,0.83,0.8],
    ('Mila','female','sophomore'):[0.82,0.85,0.79,0.83],
    ('Zoe','female','sophomore'):[0.82,0.81,0.83,0.81],
    ('Leah','female','sophomore'):[0.8,0.84,0.78,0.75],
    ('Stella','female','senior'):[0.93,0.9,0.96,0.92],
    ('Claire','female','sophomore'):[0.83,0.79,0.86,0.86],
    ('Aurora','female','senior'):[0.92,0.87,0.91,0.9],
    ('Lucy','female','senior'):[0.82,0.82,0.96,0.88],
    ('Samantha','female','senior'):[0.92,0.95,1,0.93],
    ('Tabitha','female','senior'):[0.97,0.87,0.89,0.88]}

# sophNames counts number of sophomores in studentPerf
sophNames = [x[0] for x in studentPerf if x[2] == 'sophomore']

# classes returns list of unique values of studentPerf key[2]
classes = select(studentPerf,2)

# genders returns list of unique values of studentPerf key[1]
genders = select(studentPerf,1)

# dictAvgGrade returns dict of studentPerf keys with averaged value
dictAvgGrade = {k:sum(v)/len(v) for k,v in studentPerf.items()}

# gradesSoph extracts only sophomore grades from dictAvgGrade dictionary and converts to list
gradesSoph = [v for k,v in dictAvgGrade.items() if k[2] == 'sophomore']

# initialize dictDemClass dict for use in next command
dictDemClass = {x:0 for x in classes}

# dictDemClass outer dict comp returns dict with class types as keys, 
# inner list comp returns list of students for each class type
dictDemClass =  {k:len([x for x in studentPerf if x[2] == k]) for k in dictDemClass}

# intialize dictDemGender dict for use in next command
dictDemGender = {x:0 for x in genders}

# dictDemGender outer dict comp returns dict with gender types as keys, 
# inner list comp returns list of students for each gender
dictDemGender = {k:len([x for x in studentPerf if x[1] == k]) for k in dictDemGender}

# dictGradeClass outer dict comp returns dict with class types as keys;
# inner list comp returns list from dictAvgGrade for eash class type
# inner list summed and divided by the total number in each class (use dictDemClass dict)
dictGradeClass = {k:sum([v for x,v in dictAvgGrade.items() if x[2] == k])/dictDemClass[k] for k in classes}





















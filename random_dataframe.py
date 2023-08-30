import pandas as pd
import numpy as np
import random
random.seed(123)

'''
This module contains source data and functions to generate new patient records with random data and compile into a dataframe.
'''


###################################################################################################
####################################### Source Data ###############################################
###################################################################################################
first_names_source = [
    'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Jackson', 'Oliver',
    'Lucas', 'Aiden', 'Layla', 'Ethan', 'Amelia', 'Harper', 'Muhammad', 'Abigail', 'Ella', 'Sofia',
    'Caden', 'Avery', 'Evelyn', 'Ella', 'Aria', 'Grace', 'Riley', 'Chloe', 'Lily', 'Liam',
    'Harper', 'Zoe', 'Luna', 'Mila', 'James', 'Scarlett', 'Mason', 'Emily', 'Lily', 'Aiden',
    'Liam', 'Emma', 'Sophia', 'Mia', 'Noah', 'Olivia', 'Isabella', 'Lucas', 'Ethan', 'James',
    'Avery', 'Ella', 'Riley', 'Layla', 'Scarlett', 'Chloe', 'Liam', 'Oliver', 'Emma', 'Ava',
    'Sophia', 'Isabella', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily',
    'Elizabeth', 'Sofia', 'Avery', 'Ella', 'Scarlett', 'Grace', 'Aubrey', 'Liam', 'Noah', 'Oliver',
    'Ethan', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Amelia', 'Harper', 'Evelyn', 'Liam', 'Noah',
    'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Sebastian'
]

last_names_source = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
    'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
    'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
    'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins',
    'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey',
    'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James',
    'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson',
    'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler',
    'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes', 'Myers'
]
 
state_abbreviations = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]
###################################################################################################
###################################### End Source Data ############################################
###################################################################################################



#function to randomly generate a new patient record
def generate_patient_record(first_names_source, last_names_source, state_abbreviations):

    #set parameters for variables
    min_age = 18
    max_age = 110

    min_height_inches = 54
    max_height_inches = 84

    min_weight_lbs = 100
    max_weight_lbs = 350

    #create a list for a new patient entry
    new_record = [random.choice(first_names_source),
                  random.choice(last_names_source),
                  random.randint(min_age, max_age),
                  random.randint(min_height_inches, max_height_inches),
                  random.randint(min_weight_lbs, max_weight_lbs),
                  random.choice(state_abbreviations)
                  ]
    
    return new_record


# function to generate n records and return a new dataframe with the new records
def batch_new_records(n):
    # generate list of lists from gene
    new_records = []

    for i in range(n):
            new_patient = generate_patient_record(first_names_source, last_names_source, state_abbreviations)
            new_records.append(new_patient)

    new_records = pd.DataFrame(new_records, columns=['first_name', 'last_name', 'age', 'height_inches', 'weight_lbs', 'state_residence'])

    return new_records


from protein_lengths import naa
from scrapNBA import scrape
import pandas as pd
import numpy as np
import sys

    

def scan_protein():
    #Open file from command line input. 
    with open(sys.argv[1],'r') as data:
        df_pro_count = pd.DataFrame(data = data, columns = ['Digit'])
    #Get the leftmost number. Cast as string and get index 0.
    df_pro_count = df_pro_count['Digit'].astype(str).str[0]
    df_pro = pd.DataFrame().rename_axis('Digit', axis=1)
    #Get count
    df_pro.insert(0, 'Count',df_pro_count.value_counts())
    #Get Percent
    df_pro.insert(1, 'Percent', df_pro_count.value_counts(1).mul(100))
    print(df_pro)


def scan_fib():
    #Open file from command line input. 
    with open(sys.argv[1],'r') as data:
        df_fib_count = pd.DataFrame(data = data, columns = ['Digit'])
    #Get the leftmost number. Cast as string and get index 0. 
    df_fib_count = df_fib_count['Digit'].astype(str).str[0]
    df_fib = pd.DataFrame().rename_axis('Digit', axis=1)
    #Get count
    df_fib.insert(0, 'Count',df_fib_count.value_counts())
    #Get Percent
    df_fib.insert(1, 'Percent', df_fib_count.value_counts(1).mul(100))
    print(df_fib)

def scan_county():
    #Open file from command line input. 
    with open(sys.argv[1],'r') as data:
        df_count = pd.DataFrame(data = data, columns = ['Digit'])
    #Get the leftmost number. Cast as string and get index 0. 
    df_count = df_count['Digit'].astype(str).str[0]
    df_county = pd.DataFrame().rename_axis('Digit', axis=1)
    #Get count
    df_county.insert(0, 'Count',df_count.value_counts())
    #Get Percent
    df_county.insert(1, 'Percent', df_count.value_counts(1).mul(100))
    print(df_county)

def scan_nba():
    #Open file from command line input. 
    #with open(sys.argv[1],'r') as data:
    with open('nbafile.txt','r') as data:
        df_nba = pd.DataFrame(data = data, columns = ['Digit'])
    #df_nba = df_nba['Digit'].astype(float)
    df_nba.columns = df_nba.columns.str.replace(' ','')
    
 
    """"
df_nba = pd.DataFrame(ls2)
df_nba.columns = ['height']
df_nba = df_nba['height'].astype(str)
df_nba.str.strip
df_test = pd.DataFrame()
df_test.insert(0,'height',df_nba)
df_test['height'] = df_test['height'].astype(float)
"""

def main():

    try:
        if sys.argv[1] == 'fib500.txt':
            scan_fib()
        elif sys.argv[1] == 'protein_length.txt':
            scan_protein()
        elif sys.argv[1] == 'county.txt':
            scan_county()
        elif sys.argv[1] == 'nbafile.txt':
            scan_nba()
    except:
        print("Please enter fib.txt, protein.txt, or county.txt in the command line.")

scan_nba()
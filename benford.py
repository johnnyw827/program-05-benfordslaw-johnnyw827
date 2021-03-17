from protein_lengths import naa
import pandas as pd
import numpy as np
import sys


def scan_what():
    selector = input(sys.argv)
    return selector

def scan_protein(naa):
    #Create a data frame of protein numbers.
    df_pro = pd.DataFrame(naa)
    df_pro.columns = ['Numbers']
    df_pro = df_pro['Numbers'].astype(str).str[0]
    print('Amino Analysis\n{}'.format(df_pro.value_counts(1)))


def scan_fib():
    #Create a data frame of fib numbers.
    df_fib = pd.read_csv('./fib500.txt')
    #Get the leftmost number. Cast as string and get index 0. 
    df_fib.columns = ['Numbers']
    df_fib = df_fib['Numbers'].astype(str).str[0]
    #Count unique values and represent it as a percent. 
    print('Fibinacci Analysis\n{}'.format(df_fib.value_counts(1)))


def main():
    scan_what()

main()
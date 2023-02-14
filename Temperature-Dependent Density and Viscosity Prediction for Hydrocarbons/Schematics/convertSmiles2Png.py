# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:32:45 2022

@author: pawan
"""

# Import necessary packages or module
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem.Draw import DrawingOptions


def smiles2png(smiles,fname):
    DrawingOptions.atomLabelFontSize = 55
    DrawingOptions.dotsPerAngstrom = 100
    DrawingOptions.bondLineWidth = 3.0
    
    mol = Chem.MolFromSmiles(smiles)
    rdkit.Chem.Draw.MolToFile(mol, fname, size=(1000,1000), kekulize=True, wedgeBonds=False, imageType=None, fitImage=False)
    

# read text file into pandas DataFrame
df = pd.read_csv('C:/Users/pawan/Box/12. PROJECTS/Machine Learning/Fluid Models/API Fluids_Files/PNG Files/APIfluidsSmilesCodes.txt', sep=";")

# Extract column of df variable whose coulmn name is "fluidNames"
fluidNames = df["fluidNames"]

# Extract column of df variable whose coulmn name is "smilesCodes"
smilesCodes = df["smilesCodes"]

# DataFrame to numpy array
A = df.to_numpy()

for i in range(0,len(A)): #
    smiles = A[i][1]
    fname = A[i][0]+".png"
    smiles2png(smiles,fname)
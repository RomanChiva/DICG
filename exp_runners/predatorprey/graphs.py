import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
Figure 3 reproduction
"""

""" Seed 1"""
#Penalty = -0
CENT1 = pd.read_csv("data/local/Fig3CENTP0S1/progress.csv")
DEC1 = pd.read_csv("data/local/Fig3DECP0S1/progress.csv")
DICG_DE1 = pd.read_csv("data/local/Fig3DICG_CEP0S1/progress.csv")
DICG_CE1 = pd.read_csv("data/local/Fig3DICG_DEP0S1/progress.csv")
CENT1_s = CENT1["TotalEnvSteps"]
DEC1_s = DEC1["TotalEnvSteps"]
DICG_CE1_s = DICG_CE1["TotalEnvSteps"]
DICG_DE1_s = DICG_DE1["TotalEnvSteps"]
CENT1_r = CENT1["AverageReturn"]
DEC1_r = DEC1["AverageReturn"]
DICG_CE1_r = DICG_CE1["AverageReturn"]
DICG_DE1_r = DICG_DE1["AverageReturn"]

#Penalty = -1.5
CENT1_15 = pd.read_csv("data/local/Fig3CENTP0S1/progress.csv")
DEC1_15 = pd.read_csv("data/local/Fig3DECP0S1/progress.csv")
DICG_DE1_15 = pd.read_csv("data/local/Fig3DICG_CEP0S1/progress.csv")
DICG_CE1_15 = pd.read_csv("data/local/Fig3DICG_DEP0S1/progress.csv")
CENT1_15_s = CENT1_15["TotalEnvSteps"]
DEC1_15_s = DEC1_15["TotalEnvSteps"]
DICG_CE1_15_s = DICG_CE1_15["TotalEnvSteps"]
DICG_DE1_15_s = DICG_DE1_15["TotalEnvSteps"]
CENT1_15_r = CENT1_15["AverageReturn"]
DEC1_15_r = DEC1_15["AverageReturn"]
DICG_CE1_15_r = DICG_CE1_15["AverageReturn"]
DICG_DE1_15_r = DICG_DE1_15["AverageReturn"]

""" Seed 2"""
#Penalty = -0
CENT2 = pd.read_csv("data/local/Fig3CENTP0S1/progress.csv")
DEC2 = pd.read_csv("data/local/Fig3DECP0S1/progress.csv")
DICG_DE2 = pd.read_csv("data/local/Fig3DICG_CEP0S1/progress.csv")
DICG_CE2 = pd.read_csv("data/local/Fig3DICG_DEP0S1/progress.csv")
CENT2_s = CENT2["TotalEnvSteps"]
DEC2_s = DEC2["TotalEnvSteps"]
DICG_CE2_s = DICG_CE2["TotalEnvSteps"]
DICG_DE2_s = DICG_DE2["TotalEnvSteps"]
CENT2_r = CENT2["AverageReturn"]
DEC2_r = DEC2["AverageReturn"]
DICG_CE2_r = DICG_CE2["AverageReturn"]
DICG_DE2_r = DICG_DE2["AverageReturn"]

#Penalty = -1.5
CENT2_15 = pd.read_csv("data/local/Fig3CENTP0S1/progress.csv")
DEC2_15 = pd.read_csv("data/local/Fig3DECP0S1/progress.csv")
DICG_DE2_15 = pd.read_csv("data/local/Fig3DICG_CEP0S1/progress.csv")
DICG_CE2_15 = pd.read_csv("data/local/Fig3DICG_DEP0S1/progress.csv")
CENT2_15_s = CENT2_15["TotalEnvSteps"]
DEC2_15_s = DEC2_15["TotalEnvSteps"]
DICG_CE2_15_s = DICG_CE2_15["TotalEnvSteps"]
DICG_DE2_15_s = DICG_DE2_15["TotalEnvSteps"]
CENT2_15_r = CENT2_15["AverageReturn"]
DEC2_15_r = DEC2_15["AverageReturn"]
DICG_CE2_15_r = DICG_CE2_15["AverageReturn"]
DICG_DE2_15_r = DICG_DE2_15["AverageReturn"]

""" Seed 3"""
#Penalty = -0
CENT3 = pd.read_csv("data/local/Fig3CENTP0S1/progress.csv")
DEC3 = pd.read_csv("data/local/Fig3DECP0S1/progress.csv")
DICG_DE3 = pd.read_csv("data/local/Fig3DICG_CEP0S1/progress.csv")
DICG_CE3 = pd.read_csv("data/local/Fig3DICG_DEP0S1/progress.csv")
CENT3_s = CENT3["TotalEnvSteps"]
DEC3_s = DEC3["TotalEnvSteps"]
DICG_CE3_s = DICG_CE3["TotalEnvSteps"]
DICG_DE3_s = DICG_DE3["TotalEnvSteps"]
CENT3_r = CENT3["AverageReturn"]
DEC3_r = DEC3["AverageReturn"]
DICG_CE3_r = DICG_CE3["AverageReturn"]
DICG_DE3_r = DICG_DE3["AverageReturn"]

#Penalty = -1.5
CENT3_15 = pd.read_csv("data/local/Fig3CENTP0S1/progress.csv")
DEC3_15 = pd.read_csv("data/local/Fig3DECP0S1/progress.csv")
DICG_DE3_15 = pd.read_csv("data/local/Fig3DICG_CEP0S1/progress.csv")
DICG_CE3_15 = pd.read_csv("data/local/Fig3DICG_DEP0S1/progress.csv")
CENT3_15_s = CENT3_15["TotalEnvSteps"]
DEC3_15_s = DEC3_15["TotalEnvSteps"]
DICG_CE3_15_s = DICG_CE3_15["TotalEnvSteps"]
DICG_DE3_15_s = DICG_DE3_15["TotalEnvSteps"]
CENT3_15_r = CENT3_15["AverageReturn"]
DEC3_15_r = DEC3_15["AverageReturn"]
DICG_CE3_15_r = DICG_CE3_15["AverageReturn"]
DICG_DE3_15_r = DICG_DE3_15["AverageReturn"]


"""
Density
"""
#Penalty = -0
dCENT = pd.read_csv("data/local/DensityCENTP-1.5/progress.csv")
dDEC = pd.read_csv("data/local/DensityDECP-1.5/progress.csv")
dDICG_DE = pd.read_csv("data/local/DensityDICG_CEP-1.5/progress.csv")
dDICG_CE = pd.read_csv("data/local/DensityDICG_DEP-1.5/progress.csv")
dCENT_s = dCENT["TotalEnvSteps"]
dDEC_s = dDEC["TotalEnvSteps"]
dDICG_CE_s = dDICG_CE["TotalEnvSteps"]
dDICG_DE_s = dDICG_DE["TotalEnvSteps"]
dCENT_r = dCENT["AverageReturn"]
dDEC_r = dDEC["AverageReturn"]
dDICG_CE_r = dDICG_CE["AverageReturn"]
dDICG_DE_r = dDICG_DE["AverageReturn"]

#Penalty = -1.5
dCENT_15 = pd.read_csv("data/local/DensityCENTP-1.5/progress.csv")
dDEC_15 = pd.read_csv("data/local/DensityDECP-1.5/progress.csv")
dDICG_DE_15 = pd.read_csv("data/local/DensityDICG_CEP-1.5/progress.csv")
dDICG_CE_15 = pd.read_csv("data/local/DensityDICG_DEP-1.5/progress.csv")
dCENT_15_s = dCENT_15["TotalEnvSteps"]
dDEC_15_s = dDEC_15["TotalEnvSteps"]
dDICG_CE_15_s = dDICG_CE_15["TotalEnvSteps"]
dDICG_DE_15_s = dDICG_DE_15["TotalEnvSteps"]
dCENT_15_r = dCENT_15["AverageReturn"]
dDEC_15_r = dDEC_15["AverageReturn"]
dDICG_CE_15_r = dDICG_CE_15["AverageReturn"]
dDICG_DE_15_r = dDICG_DE_15["AverageReturn"]

#Figure
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(dCENT_15_s,dCENT_15_r)
axes[0].plot(dDEC_15_s,dDEC_15_r)
axes[0].plot(dDICG_CE_15_s,dDICG_CE_15_r)
axes[0].plot(dDICG_DE_15_s,dDICG_DE_15_r)
axes[1].plot(dCENT_15_s,dCENT_15_r)
axes[1].plot(dDEC_15_s,dDEC_15_r)
axes[1].plot(dDICG_CE_15_s,dDICG_CE_15_r)
axes[1].plot(dDICG_DE_15_s,dDICG_DE_15_r)
plt.show()

"""
Grid
"""
#Penalty = -0
gCENT = pd.read_csv("data/local/DensityCENTP-1.5/progress.csv")
gDEC = pd.read_csv("data/local/DensityDECP-1.5/progress.csv")
gDICG_DE = pd.read_csv("data/local/GridDICG_CEP-1.5/progress.csv")
gDICG_CE = pd.read_csv("data/local/GridDICG_DEP-1.5/progress.csv")
gCENT_s = gCENT["TotalEnvSteps"]
gDEC_s = gDEC["TotalEnvSteps"]
gDICG_CE_s = gDICG_CE["TotalEnvSteps"]
gDICG_DE_s = gDICG_DE["TotalEnvSteps"]
gCENT_r = gCENT["AverageReturn"]
gDEC_r = gDEC["AverageReturn"]
gDICG_CE_r = gDICG_CE["AverageReturn"]
gDICG_DE_r = gDICG_DE["AverageReturn"]

#Penalty = -1.5
gCENT_15 = pd.read_csv("data/local/DensityCENTP-1.5/progress.csv")
gDEC_15 = pd.read_csv("data/local/DensityDECP-1.5/progress.csv")
gDICG_DE_15 = pd.read_csv("data/local/GridDICG_CEP-1.5/progress.csv")
gDICG_CE_15 = pd.read_csv("data/local/GridDICG_DEP-1.5/progress.csv")
gCENT_15_s = dCENT_15["TotalEnvSteps"]
gDEC_15_s = dDEC_15["TotalEnvSteps"]
gDICG_CE_15_s = dDICG_CE_15["TotalEnvSteps"]
gDICG_DE_15_s = dDICG_DE_15["TotalEnvSteps"]
gCENT_15_r = dCENT_15["AverageReturn"]
gDEC_15_r = dDEC_15["AverageReturn"]
gDICG_CE_15_r = dDICG_CE_15["AverageReturn"]
gDICG_DE_15_r = dDICG_DE_15["AverageReturn"]

#Figure
fig2, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(dCENT_15_s,dCENT_15_r)
axes[0].plot(dDEC_15_s,dDEC_15_r)
axes[0].plot(dDICG_CE_15_s,dDICG_CE_15_r)
axes[0].plot(dDICG_DE_15_s,dDICG_DE_15_r)
axes[1].plot(dCENT_15_s,dCENT_15_r)
axes[1].plot(dDEC_15_s,dDEC_15_r)
axes[1].plot(dDICG_CE_15_s,dDICG_CE_15_r)
axes[1].plot(dDICG_DE_15_s,dDICG_DE_15_r)
plt.show()

"""
Both
"""
#Penalty = -0
bCENT = pd.read_csv("data/local/BothCENTP0/progress.csv")
bDEC = pd.read_csv("data/local/BothDECP0/progress.csv")
bDICG_DE = pd.read_csv("data/local/BothDICG_CEP0/progress.csv")
bDICG_CE = pd.read_csv("data/local/BothDICG_DEP0/progress.csv")
bCENT_s = bCENT["TotalEnvSteps"]
bDEC_s = bDEC["TotalEnvSteps"]
bDICG_CE_s = bDICG_CE["TotalEnvSteps"]
bDICG_DE_s = bDICG_DE["TotalEnvSteps"]
bCENT_r = bCENT["AverageReturn"]
bDEC_r = bDEC["AverageReturn"]
bDICG_CE_r = bDICG_CE["AverageReturn"]
bDICG_DE_r = bDICG_DE["AverageReturn"]

#Penalty = -1.5
bCENT_15 = pd.read_csv("data/local/BothCENTP0/progress.csv")
bDEC_15 = pd.read_csv("data/local/BothDECP0/progress.csv")
bDICG_DE_15 = pd.read_csv("data/local/BothDICG_CEP-1.5/progress.csv")
bDICG_CE_15 = pd.read_csv("data/local/BothDICG_DEP-1.5/progress.csv")
bCENT_15_s = dCENT_15["TotalEnvSteps"]
bDEC_15_s = dDEC_15["TotalEnvSteps"]
bDICG_CE_15_s = dDICG_CE_15["TotalEnvSteps"]
bDICG_DE_15_s = dDICG_DE_15["TotalEnvSteps"]
bCENT_15_r = dCENT_15["AverageReturn"]
bDEC_15_r = dDEC_15["AverageReturn"]
bDICG_CE_15_r = dDICG_CE_15["AverageReturn"]
bDICG_DE_15_r = dDICG_DE_15["AverageReturn"]

#Figure
fig3, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(dCENT_15_s,dCENT_15_r)
axes[0].plot(dDEC_15_s,dDEC_15_r)
axes[0].plot(dDICG_CE_15_s,dDICG_CE_15_r)
axes[0].plot(dDICG_DE_15_s,dDICG_DE_15_r)
axes[1].plot(dCENT_15_s,dCENT_15_r)
axes[1].plot(dDEC_15_s,dDEC_15_r)
axes[1].plot(dDICG_CE_15_s,dDICG_CE_15_r)
axes[1].plot(dDICG_DE_15_s,dDICG_DE_15_r)
plt.show()
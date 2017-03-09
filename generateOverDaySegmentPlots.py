import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("../../data/proc/allcats_cleaned.txt", sep = ',', header=0,encoding='cp1252')

#HR Over Day
plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='HRSeg1', data = df, hue='CatName')
plt.title("HR Segment 1 - Over Day")
plt.xlabel('Run ID')
plt.ylabel("HR Seg1")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_HRSeg1.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='HRSeg2A', data = df, hue='CatName')
plt.title("HR Segment 2A - Over Day")
plt.xlabel('Run ID')
plt.ylabel("HR Seg2A")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_HRSeg2A.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='HRSeg2', data = df, hue='CatName')
plt.title("HR Segment 2 - Over Day")
plt.xlabel('Run ID')
plt.ylabel("HR Seg2")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_HRSeg2.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='HRSeg3', data = df, hue='CatName')
plt.title("HR Segment 3 - Over Day")
plt.xlabel('Run ID')
plt.ylabel("HR Seg3")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_HRSeg3.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='HRSeg4', data = df, hue='CatName')
plt.title("HR Segment 4  - Over Day")
plt.xlabel('Run ID')
plt.ylabel("HR Seg4")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_HRSeg4.png', dpi=500)
plt.close()

#Flow Over Day
plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='FlowSeg1', data = df, hue='CatName')
plt.title("Flow Segment 1 - Over Day")
plt.xlabel('Run ID')
plt.ylabel("Flow Seg1")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_FlowSeg1.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='FlowSeg2A', data = df, hue='CatName')
plt.title("Flow Segment 2A - Over Day")
plt.xlabel('Run ID')
plt.ylabel("Flow Seg2A")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_FlowSeg2A.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='FlowSeg2', data = df, hue='CatName')
plt.title("Flow Segment 2 - Over Day")
plt.xlabel('Run ID')
plt.ylabel("Flow Seg2")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_FlowSeg2.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='FlowSeg3', data = df, hue='CatName')
plt.title("Flow Segment 3 - Over Day")
plt.xlabel('Run ID')
plt.ylabel("Flow Seg3")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_FlowSeg3.png', dpi=500)
plt.close()

plt.clf()
sns.set(style='whitegrid',context='paper')
sns.lmplot(x='RunID',y='FlowSeg4', data = df, hue='CatName')
plt.title("Flow Segment 4  - Over Day")
plt.xlabel('Run ID')
plt.ylabel("Flow Seg4")
#plt.figure(figsize=(8,10))
plt.savefig('../../results/fig/OverDay_FlowSeg4.png', dpi=500)
plt.close()

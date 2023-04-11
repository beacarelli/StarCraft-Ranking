# IMPORTING LIBRARIES
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
from matplotlib import cm
from IPython.display import clear_output

# IMPORTING, READING AND NAMING COLLOMNS OF DATA
data = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/00272/SkillCraft1_Dataset.csv',
    header= 0
)

          
data.collomns = [
    'GameID',
    'LeagueIndex',
    'Age',
    'HoursPerWeek',
    'TotalHours',
    'APM',
    'SelectByHotkeys',
    'AssignToHotkeys',
    'AssignToHotkey',
    'MinimapAttacks',
    'MinimapRightClicks',
    'NumberOfPACs',
    'GapBetweenPACs',
    'ActionLatency',
    'ActionsInPAC',
    'TotalMapExplored',
    'WorkersMade',
    'UniqueUnitsMade',
    'ComplexUnitsMade',
    'ComplexAbilitiesUsed',
]
  

data.head(5)

# FILTER: ONLY 1ª AND 3ª CLASS
data = data[data['LeagueIndex']!=2]

# CLASS FREQUENCY
data['LeagueIndex'].value_counts()

# PAIR PLOT
sns.pairplot(
    data,
    hue="LeagueIndex",
)

# FILTER: 4 VARIABLES
data = data[[
    'LeagueIndex',
    'APM',
    'SelectByHotkeys',
    'ActionLatency'
]]

# CREATE FIGURE WINDOW
fig = plt.figure()

# LOAD AXIS AND CREATE AN ADDITIONAL ONE IF NECESSARY
ax = fig.gca(projection='3d')

# CREATE COLOR LIST BY QUALITY 

colors = data['LeagueIndex'].map({6:'g', 5: 'yellow', 4: 'orange', 3:'b', 1:'r'}).values

# CREATE GRAPHIC
ax.scatter(
    data['APM'],
    data['SelectByHotkeys'],
    data['ActionLatency'],
    c = colors
)
# NAMING AXIS
plt.title("Ranking")
plt.xlabel('APM')
plt.ylabel('SelectByHotkeys')
ax.set_zlabel('ActionLatency')

# CONFIGURATE LEGENDS
legend_elements = [
    Line2D([0], [0],
        marker='o',
        color='w',
        label='Master',
        markerfacecolor='g',
        markersize=10
    ),
    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Diamond',
        markerfacecolor='yellow',
        markersize=10
    ),
     Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Platinum',
        markerfacecolor='orange',
        markersize=10
    ),
         Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Bronze',
        markerfacecolor='r',
        markersize=10
    )
]
                   
# CREATE LEGENDS
ax.legend(handles=legend_elements, loc='best', fontsize= 7.49)



plt.tight_layout()
plt.show()
# ADJUST AND SHOW THE GRAPHIC
plt.tight_layout()
plt.show()

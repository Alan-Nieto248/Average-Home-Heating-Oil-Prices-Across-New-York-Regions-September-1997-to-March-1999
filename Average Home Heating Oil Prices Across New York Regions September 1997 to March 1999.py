import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loads the data
data = pd.read_csv('Average_Home_Heating_Oil_Prices.csv')

x = data["Date"]
a = data['New York City Average ($/gal)']
b = data['Long Island Average ($/gal)']
c = data['Capital District Average ($/gal)']
d = data['New York Statewide Average ($/gal)']
e = data['Lower Hudson Average ($/gal)']
plt.figure (figsize=(12, 7))
plt.xlabel('Date (dd/mm/yyyy)',font='times new roman',fontsize=20)
plt.ylabel('Average Price ($/gal)',font='times new roman',fontsize=20)
plt.title('Average Home Heating Oil Prices in New York State',font='times new roman',fontsize=25)
plt.xticks(rotation=50)
plt.plot(x, a, label='New York City Average', color='blue')
plt.plot(x, b, label='Long Island Average', color='orange')
plt.plot(x, c, label='Capital District Average', color='red')
plt.plot(x, d, label='New York Statewide Average', color='green')
plt.plot(x, e, label='Lower Hudson Average', color='purple')


plt.legend(loc='upper right', labels=('New York City Average', 'Long Island Average', 'Capital District Average', 'New York Statewide Average', 'Lower Hudson Average'), ncol=1, title='Regions', title_fontsize='13', fontsize='10', shadow=True, fancybox=True, facecolor='white', edgecolor='black')
plt.tight_layout()
plt.grid(visible=True, color='gray', linestyle='--', linewidth=0.5)

plt.show()
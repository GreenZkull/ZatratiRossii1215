import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data-20141230-structure-20141230.csv')
subjects =  ['1912_y', '1913_y', '1914_y','1915_y']
dataset = df.groupby('typename')[subjects].mean()

indx = np.arange(len(subjects))
score_label = np.arange(0, 110000000, 10000000)
Just_means = list(dataset.T['Обыкновенные расходы'])
Special_means = list(dataset.T['Чрезвычайные расходы'])

bar_width = 0.45

fig, ax = plt.subplots()
barJust = ax.bar(indx - bar_width/2, Just_means, bar_width, label='Обыкновенные')
barSpecial = ax.bar(indx + bar_width/2, Special_means, bar_width, label='Чрезвычайные')

# метки оси x
ax.set_xticks(indx)
ax.set_xticklabels(subjects)

# метки оси y
ax.set_yticks(score_label)
ax.set_yticklabels(score_label)


# Легенда
ax.legend()

def insert_data_labels(bars):
	for bar in bars:
		bar_height = bar.get_height()
		ax.annotate('{0:.0f}'.format(bar.get_height()),
			xy=(bar.get_x() + bar.get_width()/2, bar_height),
			xytext=(0, 3),
			textcoords='offset points',
			ha='center',
			va='bottom'
		)


plt.title("Бюджет России с 1912-1915 годов")
plt.ylabel("Рубли")
plt.xlabel("Годы с 1912 по 1915")
plt.show()

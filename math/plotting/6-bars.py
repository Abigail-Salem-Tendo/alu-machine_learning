#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here

plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[0], color='red', width=0.5, label='apples')
plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[1], color='yellow', width=0.5, label='bananas', bottom=fruit[0])
plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[2], color='#ff8000', width=0.5, label='oranges', bottom=fruit[0] + fruit[1])
plt.bar(['Farrah', 'Fred', 'Felicia'], fruit[3], color='#ffe5b4', width=0.5, label='peaches', bottom=fruit[0] + fruit[1] + fruit[2])

plt.ylabel('Quantity of Fruit')
plt.yticks(np.arange(0, 81, 10))
plt.ylim(0, 80)
plt.title('Number of Fruit per Person')
plt.legend()

plt.show()
import matplotlib.pyplot as plt
import numpy as np

def bar_heights(intervals, probabilities, total_probability):

    heights = []

    #TODO: sum the relative probabilities
    total_relative_prob = sum(probabilities)

    for i in range(0, len(probabilities)):

        #TODO: Looping through the probabilities list,
        #      take one probability at a time and
        #      calculate the area of each bar. Think about how you can
        #      calculate the area of a bar knowing the total_probability,
        #      relative probability, and the sum of the relative probabilities

        bar_area = ( (probabilities[i]/total_relative_prob) ) * total_probability

        # TODO: Calculate the height of the bar and append the value to the
        # heights list.Remember that the area of each bar
        # is the width of the bar times the height of the bar
        heights.append(bar_area/(intervals[i+1]-intervals[i]))

    return heights

hour_intervals = [0, 5, 10, 16, 21, 24]
probability_intervals = [1, 5, 3, 6, 1/2]
accident_probability = 0.05

heights = bar_heights(hour_intervals, probability_intervals, accident_probability)
freqs = np.array(heights)
bins = np.array(hour_intervals)
widths = bins[1:] - bins[:-1]
freqs = freqs.astype(np.float)

widths = bins[1:] - bins[:-1]

tick_interval = 1
plt.bar(bins[:-1], freqs, width=widths, align='edge', edgecolor='black', alpha=0.5)
plt.xlabel('Interval')
plt.ylabel('Probability Distribution')
plt.title('Probability Distribution')
plt.xticks(np.arange(min(bins), max(bins)+1, tick_interval))

plt.show()

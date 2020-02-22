from scipy.stats import t
from numpy import average, std
from math import sqrt

if __name__ == '__main__':
    # data we want to evaluate: average height of 30 one year old male and
    # female toddlers. Interestingly, at this age height is not bimodal yet
    data = [63.5, 81.3, 88.9, 63.5, 76.2, 67.3, 66.0, 64.8, 74.9, 81.3, 76.2,
            72.4, 76.2, 81.3, 71.1, 80.0, 73.7, 74.9, 76.2, 86.4, 73.7, 81.3,
            68.6, 71.1, 83.8, 71.1, 68.6, 81.3, 73.7, 74.9]
    mean = average(data)
    # evaluate sample variance by setting delta degrees of freedom (ddof) to
    # 1. The degree used in calculations is N - ddof
    stddev = std(data, ddof=1)
    # Get the endpoints of the range that contains 95% of the distribution
    t_bounds = t.interval(0.95, len(data) - 1)
    # sum mean to the confidence interval
    ci = [mean + critval * stddev / sqrt(len(data)) for critval in t_bounds]
    print ("Mean: %f" % mean)
    print ("Confidence Interval 95%%: %f, %f" % (ci[0], ci[1]))

import math
def mean(values):
    return sum(map(float, values)) / len(values)

def median(value):
    return sorted(value)[len(value) // 2]

def variance(values):
    m = mean(values)
    return sum(map(lambda x: (x - m) ** 2, values)) / len(values)

def stddev(values):
    return math.sqrt(variance(values))

stat_functions = {
    'mean': mean,
    'median': median,
    'min': min,
    'max': max,
    
}
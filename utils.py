import pandas as pd


def get_num_group(floor, ceiling, dataset, index_name):
    group = dataset.apply(lambda x: True if ceiling > x[index_name] > floor else False, axis=1)
    count = len(group[group == True].index)
    return count


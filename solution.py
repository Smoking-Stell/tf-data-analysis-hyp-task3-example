import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.02
    expect_mean = 500
    t_stat, p_value = ttest_1samp(x, expect_mean)
    return p_value < alpha # Ваш ответ, True или False

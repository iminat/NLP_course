import numpy as np
from scipy.stats import spearmanr, kendalltau

# Задаем данные о рангах успеваемости по математике и физике
math_ranks = [2, 4, 1, 3, 5, 6, 7, 9, 8, 10]
physics_ranks = [4, 2, 1, 3, 5, 6, 8, 7, 9, 10]

# Применяем критерий Спирмена
rho, p_value_spearman = spearmanr(math_ranks, physics_ranks)

# Применяем критерий Кендалла
tau, p_value_kendall = kendalltau(math_ranks, physics_ranks)

print("Коэффициент корреляции Спирмена: ", rho)
print("p-значение для критерия Спирмена: ", p_value_spearman)
print("Коэффициент корреляции Кендалла: ", tau)
print("p-значение для критерия Кендалла: ", p_value_kendall)

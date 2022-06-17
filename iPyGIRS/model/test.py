# -*- coding: utf-8 -*-

import numpy as np

from EmpiricStats import EmpiricStats

if __name__ == "__main__":
    x = np.array([1,2,3,4,5,6])
    y = np.array([9.1,18.3,32,47,69.5,94.8])
    #
    equation1 = "y = α * x + β"
    init_params1 = [10,10]
    
    equation2 = "y = α * x ** 2 + β * x + γ"
    init_params2 = [10,10,10]
    
    equation3 = "y = α * exp(β * x)"
    init_params3 = [10,10]
    
    equation4 = "y = α + β * log(x) - exp(γ * x)"
    init_params4 = [10,10,10]
    #
    empiricStats1 = EmpiricStats(equation1, init_params1)
    fit_result1 = empiricStats1.fit(x, y) 
    print("当前方程是：", empiricStats1.get_equation())
    print("拟合参数：", empiricStats1.get_params())
    print("\n")
    #
    empiricStats2 = EmpiricStats(equation2, init_params2)
    fit_result2 = empiricStats2.fit(x, y) 
    print("当前方程是：", empiricStats2.get_equation())
    print("拟合参数：", empiricStats2.get_params())
    print("\n")
    #
    empiricStats3 = EmpiricStats(equation3, init_params3)
    fit_result3 = empiricStats3.fit(x, y) 
    print("当前方程是：", empiricStats3.get_equation())
    print("拟合参数：", empiricStats3.get_params())
    print("\n")
    #
    empiricStats4 = EmpiricStats(equation4, init_params4)
    fit_result4 = empiricStats4.fit(x, y) 
    print("当前方程是：", empiricStats4.get_equation())
    print("拟合参数：", empiricStats4.get_params())
    print("\n")

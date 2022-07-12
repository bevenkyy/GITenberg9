# -*- coding:utf-8 -*-

'''
This module implements ...,

'''

__author__ = "xingrui"

import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import numexpr as ne
from scipy import optimize

from MathLib.stats_score import r2_score, mse_score


class EmpiricStats:
        
    def __init__(self,
                 init_equation,
                 init_params):
        '''
        '''
        self.init_equation = init_equation.split("=")[1].strip()
        self.init_params = init_params
        self.params_name = None
        #
        self._fitted_params = {}
        self._fitted_equation = None
        self._fitted_equation_data = {}

    def _parse_equation_str(self, params):
        '''
        '''
        re_str = "[α-ω]"
        params_dict = {}
        self.params_name = re.findall(re_str, self.init_equation)
        for param, value in zip(self.params_name, params):
            params_dict[param] = value
        #
        return params_dict


    def _loss_function(self, params, x, y):
        '''
        '''
        params_dict  = self._parse_equation_str(params)
        for key, value in params_dict.items():
            if np.isnan(value):
                value = np.nan_to_num(value)
            exec(str(key) + "=" + str(value))
        loss = ne.evaluate(self.init_equation) - y
        #
        return loss
    

    def fit(self, x, y):
        '''
        '''
        fit_result = optimize.leastsq(self._loss_function,
                                      self.init_params,
                                      args=(x,y))
        #
        _temp_equation = self.init_equation
        for param, value in zip(self.params_name, fit_result[0]):
            self._fitted_params[param] = value
            #
            self._fitted_equation = _temp_equation.replace(param,
                                                           str(value))
            _temp_equation = self._fitted_equation
        #
        training_data = []
        #
        training_y_true = y
        training_y_pred = self.predict(x, y)
        #
        r2 = r2_score(training_y_true, training_y_pred)
        mse = mse_score(training_y_true, training_y_pred)
        #
        training_data.append(r2)
        training_data.append(mse)
        training_data.append(np.hstack((training_y_true[:,np.newaxis],
                                        training_y_pred[:,np.newaxis])))
        #
        self._fitted_equation_data["training_data"] = training_data
        #
        return training_y_pred

    def predict(self, x, y):
        '''
        '''
        test_y_true = y
        test_y_pred = ne.evaluate(self._fitted_equation,
                                  local_dict = {'x':x})
        test_data = []
        #
        r2 = r2_score(test_y_true, test_y_pred)
        mse = mse_score(test_y_true, test_y_pred)
        #
        test_data.append(r2)
        test_data.append(mse)
        test_data.append(np.hstack((test_y_true[:,np.newaxis],
                                    test_y_pred[:,np.newaxis])))
        #
        self._fitted_equation_data["test_data"] = test_data
        #
        return test_y_pred

    def get_params(self):
        '''
        '''
        return self._fitted_params

    def get_equation(self):
        '''
        '''
        return self._fitted_equation

    def get_equation_data(self):
        '''
        '''
        return self._fitted_equation_data


if __name__ == "__main__":
    #
    print("Error!This script cannot be executed alone!")

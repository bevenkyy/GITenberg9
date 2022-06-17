# -*- coding:utf-8 -*-

'''
This module implements classifier: LogisticRegression, GaussianProcessRegressor,
SVC, MLPClassifier, DecisionTreeClassifier, RandomForestClassifier,AdaBoostClassifier,
implements regressor:LinearRegression, Ridge, Lasso, GaussianProcessRegressor,
KernelRidge, MLPRegressor, DecisionTreeRegressor, RandomForestRegressor, AdaBoostRegressor

'''

__author__ = "xingrui"

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from sklearn import (linear_model, tree, svm,
                     neural_network, ensemble, cluster)
from sklearn.model_selection import KFold, GridSearchCV, learning_curve

from MathLib.stats_score import *


class ScikitLearnML:

    valid_task_type = ["Classification", "Regression", "Cluster"]
    #
    valid_classifier = ["LogisticRegressionClassifier", "DecisionTreeClassifier", 
                       "SVMClassifier", "MLPClassifier", "RandomForestClassifier",
                        "GradientBoostingClassifier"]
    valid_regressor = ["LinearRegressionRegressor", "RidgeRegressionRegressor",
                       "LassoRegressionRegressor", "DecisionTreeRegressor",
                       "SVMRegressor", "MLPRegressor", "RandomForestRegressor",
                       "GradientBoostingRegressor"]
    valid_cluster = ["KMeansCluster",]
    valid_params_type = ["default", "tuning", "custom"]
    #
    seed = 0
        
    def __init__(self,
                 task_type = "Classification",
                 estimator_name = "LogisticRegressionRegressor",
                 params_type = "default",
                 basic_params = None,
                 training_params = None):
        '''
        '''
        self._task_type = task_type
        self._estimator_name = estimator_name
        self._params_type = params_type
        self._basic_params =basic_params
        self._training_params = training_params
        #
        self._init_estimator = None
        self._trained_estimator = None
        self._trained_estimator_data = {}
        #
        self._build_estimator()
        self._parse_params()

    def _build_estimator(self):
        '''
        '''
        if self._task_type == "Classification":
            if self._estimator_name == "LogisticRegression":
                self._init_estimator = linear_model.LogisticRegression(random_state = self.seed)
            elif self._estimator_name == "DecisionTreeClassifier":
                self._init_estimator = tree.DecisionTreeClassifier(random_state = self.seed)
            elif self._estimator_name == "SVC":
                self._init_estimator = svm.SVC(random_state = 0)
            elif self._estimator_name == "MLPClassifier":
                self._init_estimator = neural_network.MLPClassifier(random_state = self.seed)
            elif self._estimator_name == "RandomForestClassifier":
                self._init_estimator = ensemble.RandomForestClassifier(random_state = self.seed)
            elif self._estimator_name == "GradientBoostingClassifier":
                self._init_estimator = ensemble.GradientBoostingClassifier(random_state = self.seed)
            else:
                raise Exception("Invalid estimator")
        elif self._task_type == "Regression":
            if self._estimator_name == "LinearRegression":
                self._init_estimator = linear_model.LinearRegression()
            elif self._estimator_name == "Ridge":
                self._init_estimator = linear_model.Ridge(random_state = self.seed)
            elif self._estimator_name == "Lasso":
                self._init_estimator = linear_model.Lasso(random_state = self.seed)
            elif self._estimator_name == "DecisionTreeRegressor":
                self._init_estimator = tree.DecisionTreeRegressor(random_state = self.seed)
            elif self._estimator_name == "SVR":
                self._init_estimator = svm.SVR()
            elif self._estimator_name == "MLPRegressor":
                self._init_estimator = neural_network.MLPRegressor(random_state = self.seed)
            elif self._estimator_name == "RandomForestRegressor":
                self._init_estimator = ensemble.RandomForestRegressor(random_state = self.seed)
            elif self._estimator_name == "GradientBoostingRegressor":
                self._init_estimator = ensemble.GradientBoostingRegressor(random_state = self.seed)
            else:
                raise Exception("Invalid estimator")
        elif self._task_type == "Cluster":
            if self._estimator_name == "KMeans":
                self._init_estimator = cluster.KMeans(random_state = self.seed)
            else:
                raise Exception("Invalid estimator")
        else:
            raise Exception("Invalid parameter 'task_type'")
    
    def _parse_params(self):
        #
        n_splits = self._training_params.get("cv")
        if n_splits == None:
            raise Exception("Invalid basic params,“cv” parameter cannot be None!")
        self._cv = KFold(n_splits, shuffle = True, random_state = self.seed)
        #
        self._n_jobs = self._training_params.get("n_jobs")
        if self._n_jobs == None:
            raise Exception("Invalid basic params,“n_jobs” parameter cannot be None!")
        #

    def fit(self, training_X, training_y):
        '''
        '''
        trained_data = []
        cv_data = []
        #
        if self._params_type == "default":
            self._trained_estimator = self._init_estimator
            self._trained_estimator.fit(training_X, training_y)
            #
            training_y_pred = self._trained_estimator.predict(training_X)
            #
            training_r2_score = r2_score(training_y, training_y_pred)
            training_mse_score = mse_score(training_y, training_y_pred)
            #
            trained_data.append(training_r2_score)
            trained_data.append(training_mse_score)
            trained_data.append(np.hstack((training_y[:,np.newaxis], 
                                           training_y_pred[:,np.newaxis])))
        elif self._params_type == "tuning" or self._params_type == "custom":
            self._trained_estimator = GridSearchCV(self._init_estimator,
                                                   self._basic_params,
                                                   cv = self._cv,
                                                   scoring=("r2","neg_mean_squared_error",
                                                            "neg_mean_absolute_error"),
                                                   refit = "r2",
                                                   n_jobs = self._n_jobs)
            #
            self._trained_estimator.fit(training_X, training_y)
            #
            for i, (training_index, cv_index) in enumerate(self._cv.split(training_X)):
                #
                training_X_ = training_X[training_index]
                training_y_ = training_y[training_index]
                training_y_pred = self._trained_estimator.predict(training_X_)
                #
                training_r2_score = r2_score(training_X_, training_y_pred)
                training_mse_score = mse_score(training_y_, training_y_pred)
                #
                #
                cv_X = training_X[cv_index]
                cv_y = training_y[cv_index]
                cv_y_pred = self._trained_estimator.predict(cv_X)
                # 
                cv_r2_score = r2_score(cv_y, cv_y_pred)
                cv_mse_score = mse_score(cv_y, cv_y_pred)
                #
                trained_data.append({"training_" + str(i):(training_r2_score, training_mse_score,
                                                           np.hstack((training_y_[:,np.newaxis], 
                                                                      training_y_pred[:,np.newaxis])))})
                cv_data.append({"cv_" + str(i):(cv_r2_score, cv_mse_score,
                                                np.hstack((cv_y[:,np.newaxis], 
                                                           cv_y_pred[:,np.newaxis])))})
        else:
            raise Exception("Invalid Parameter 'params_type'")
        #
        self._trained_estimator_data["trained_data"] = trained_data
        self._trained_estimator_data["cv_data"] = cv_data

    def fit_validate(self, training_X, training_y, test_X, test_y, out_data):
        '''
        '''
        trained_data = []
        cv_data = []
        test_data = []
        #
        if self._params_type == "default":
            self._trained_estimator = self._init_estimator
            self._trained_estimator.fit(training_X, training_y)
            #
            training_y_pred = self._trained_estimator.predict(training_X)
            #
            #---------tmp---------
            training_bias_score = bias_score(training_y, training_y_pred)
            training_r_score, _ = r_score(training_y, training_y_pred)
            training_r2_score = r2_score(training_y, training_y_pred)
            training_mae_score =  mae_score(training_y, training_y_pred)
            training_mape_score = mape_score(training_y, training_y_pred)
            training_rmse_score = rmse_score(training_y, training_y_pred)
            #
            print(training_bias_score)
            print(training_r_score)
            print(training_r2_score)
            print(training_mae_score)
            print(training_mape_score)
            print(training_rmse_score)
            #---------tmp---------
            #
            trained_data.append(training_r2_score)
            trained_data.append(training_rmse_score)
            trained_data.append(np.hstack((training_y[:,np.newaxis], 
                                           training_y_pred[:,np.newaxis])))
        elif self._params_type == "tuning" or self._params_type == "custom":
            self._trained_estimator = GridSearchCV(self._init_estimator,
                                                   self._basic_params,
                                                   cv = self._cv,
                                                   scoring=("r2","neg_mean_squared_error",
                                                            "neg_mean_absolute_error"),
                                                   refit = "r2",
                                                   n_jobs = self._n_jobs)
            #
            self._trained_estimator.fit(training_X, training_y)
            #
            training_bias_score_list = []
            training_r_score_list = []
            training_r2_score_list = []
            training_mae_score_list = []
            training_mape_score_list = []
            training_rmse_score_list = []
            #
            cv_bias_score_list = []
            cv_r_score_list = []
            cv_r2_score_list = []
            cv_mae_score_list = []
            cv_mape_score_list = []
            cv_rmse_score_list = []
            #---------tmp---------
            #
            best_cv_r2_score = -1
            best_training_index = None
            best_cv_index = None
            #
            for training_index, cv_index in self._cv.split(training_X):
                #
                training_X_ = training_X[training_index]
                training_y_ = training_y[training_index]
                training_y_pred = self._trained_estimator.predict(training_X_)
                #
                ###
                training_bias_score = bias_score(training_y_, training_y_pred)
                training_r_score, _ = r_score(training_y_, training_y_pred)
                training_r2_score = r2_score(training_y_, training_y_pred)
                training_mae_score = mae_score(training_y_, training_y_pred)
                training_mape_score = mape_score(training_y_, training_y_pred)
                training_rmse_score = rmse_score(training_y_, training_y_pred)
                #         
                training_bias_score_list.append(training_bias_score)
                training_r_score_list.append(training_r_score)
                training_r2_score_list.append(training_r2_score)
                training_mae_score_list.append(training_mae_score)
                training_mape_score_list.append(training_mape_score)
                training_rmse_score_list.append(training_rmse_score)
                ###
                #
                #
                cv_X = training_X[cv_index]
                cv_y = training_y[cv_index]
                cv_y_pred = self._trained_estimator.predict(cv_X)
                #
                #
                ###
                cv_bias_score = bias_score(cv_y, cv_y_pred)
                cv_r_score, _ = r_score(cv_y, cv_y_pred)
                cv_r2_score = r2_score(cv_y, cv_y_pred)
                cv_mae_score = mae_score(cv_y, cv_y_pred)
                cv_mape_score = mape_score(cv_y, cv_y_pred)
                cv_rmse_score = rmse_score(cv_y, cv_y_pred)
                #
                cv_bias_score_list.append(cv_bias_score)
                cv_r_score_list.append(cv_r_score)
                cv_r2_score_list.append(cv_r2_score)
                cv_mae_score_list.append(cv_mae_score)
                cv_mape_score_list.append(cv_mape_score)
                cv_rmse_score_list.append(cv_rmse_score)
                ###
                #
                #
                if cv_r2_score > best_cv_r2_score:
                    best_training_index = training_index
                    best_cv_index = cv_index
            #
            #
            ###
            mean_training_bias_score = np.mean(np.array(training_bias_score_list, dtype = np.float64))
            mean_training_r_score = np.mean(np.array(training_r_score, dtype = np.float64))
            mean_training_r2_score = np.mean(np.array(training_r2_score_list, dtype = np.float64))
            mean_training_mae_score = np.mean(np.array(training_mae_score, dtype = np.float64))
            mean_training_mape_score = np.mean(np.array(training_mape_score, dtype = np.float64))
            mean_training_rmse_score = np.mean(np.array(training_rmse_score_list, dtype = np.float64))
            #
            mean_cv_bias_score = np.mean(np.array(cv_bias_score_list, dtype = np.float64))
            mean_cv_r_score = np.mean(np.array(cv_r_score_list, dtype = np.float64))
            mean_cv_r2_score = np.mean(np.array(cv_r2_score_list, dtype = np.float64))
            mean_cv_mae_score = np.mean(np.array(cv_mae_score_list, dtype = np.float64))
            mean_cv_mape_score = np.mean(np.array(cv_mape_score_list, dtype = np.float64))
            mean_cv_rmse_score = np.mean(np.array(cv_rmse_score_list, dtype = np.float64))
            ###
            #
            print(mean_training_bias_score)
            print(mean_training_r_score)
            print(mean_training_r2_score)
            print(mean_training_mae_score)
            print(mean_training_mape_score)
            print(mean_training_rmse_score)
            #
            print(mean_cv_bias_score)
            print(mean_cv_r_score)
            print(mean_cv_r2_score)
            print(mean_cv_mae_score)
            print(mean_cv_mape_score)
            print(mean_cv_rmse_score)
            #
            trained_data.append(mean_training_r2_score)
            trained_data.append(mean_training_rmse_score)
            best_training_y_pred = self._trained_estimator.predict(training_X[best_training_index])
            trained_data.append(np.hstack((training_y[best_training_index][:,np.newaxis], 
                                           best_training_y_pred[:,np.newaxis])))

            cv_data.append(mean_cv_r2_score)
            cv_data.append(mean_cv_rmse_score)
            best_cv_y_pred = self._trained_estimator.predict(training_X[best_cv_index])
            cv_data.append(np.hstack((training_y[best_cv_index][:,np.newaxis], 
                                      best_cv_y_pred[:,np.newaxis])))
        else:
            raise Exception("Invalid Parameter 'params_type'")
        #
        if test_X is not None and test_y is not None:
            test_y_true = test_y
            test_y_pred = self._trained_estimator.predict(test_X)
            #
            test_bias_score = bias_score(test_y_true, test_y_pred)
            test_r_score, _ = r_score(test_y_true, test_y_pred)
            test_r2_score = r2_score(test_y_true, test_y_pred)
            test_mae_score = mae_score(test_y_true, test_y_pred)
            test_mape_score = mape_score(test_y_true, test_y_pred)
            test_rmse_score = rmse_score(test_y_true, test_y_pred)
            #
            print(test_bias_score)
            print(test_r_score)
            print(test_r2_score)
            print(test_mae_score)
            print(test_mape_score)
            print(test_rmse_score)
            #
            test_data.append(test_r2_score)
            test_data.append(test_rmse_score)
            test_data.append(np.hstack((test_y_true[:,np.newaxis], 
                                        test_y_pred[:,np.newaxis])))
        #
        #
        self._trained_estimator_data["trained_data"] = trained_data
        self._trained_estimator_data["cv_data"] = cv_data
        self._trained_estimator_data["test_data"] = test_data
        #
        out_data["trained_estimator"] = self.get_estimator()
        out_data["estimator_data"] = self.get_estimator_data()
    
    def get_estimator(self):
        #
        return self._trained_estimator

    def get_cv(self):
        #
        return self._cv

    def get_njobs(self):
        #
        return self._n_jobs

    def get_estimator_data(self):
        #
        return self._trained_estimator_data

    def predict(self, X, y):
        '''
        '''
        test_data = {}
        #
        test_y_true = y
        test_y_pred = self._trained_estimator.predict(X)
        #
        test_r2_score = r2_score(test_y_true, test_y_pred)
        test_mse_score = mse_score(test_y_true, test_y_pred)
        test_data.update({"test":(test_r2_score, test_mse_score,
                                    np.hstack((test_y_true[:,np.newaxis], 
                                               test_y_pred[:,np.newaxis])))})
        #
        return test_y_pred

    def learning_curve(self, X, y):
        '''
        '''
        training_sizes, training_scores, cv_scores = learning_curve(self._trained_estimator, X, y,
                                                                    scoring = "neg_mean_squared_error",
                                                                    cv = self._cv,
                                                                    n_jobs = self._n_jobs)
        return training_sizes, training_scores, cv_scores

    @staticmethod
    def learning_curve_out(trained_estimator, X,  y, n_splits, n_jobs, out_data):
        '''
        '''
        cv = KFold(n_splits, shuffle = True)
        #
        training_sizes, training_scores, cv_scores = learning_curve(trained_estimator, X, y,
                                                                    scoring = "neg_mean_squared_error",
                                                                    cv = cv,
                                                                    n_jobs = n_jobs)
        train_scores_mean = -1 * np.mean(training_scores, axis = 1)
        cv_scores_mean = -1 * np.mean(cv_scores, axis = 1)
        #
        out_data["training_size"] = training_sizes
        out_data["training_scores"] = train_scores_mean
        out_data["cv_scores"] = cv_scores_mean


if __name__ == "__main__":
    #
    print("Error!This script cannot be executed alone!")

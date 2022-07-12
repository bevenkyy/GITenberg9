#-*-coding: utf-8 -*-

import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sklearn.externals import joblib


def _load_estimator(file_path):
    '''
    '''
    return joblib.load(file_path)


def _save_estimator(estimator, file_path):
    '''
    '''
    joblib.dump(estimator, file_path)

def load_estimator(filepath):
    '''
    '''
    estimator_info = {}
    #
    with open(filepath, 'r', encoding = "utf8") as fid:
        json_obj = json.load(fid)
        #
        estimator_info["estimator_name"] = json_obj.get("estimator_name")
        estimator_info["training_samples_count"] = json_obj.get("training_samples_count")
        estimator_info["test_samples_count"] = json_obj.get("test_samples_count")
        estimator_info["samples_features"] = json_obj.get("samples_features")
        estimator_info["cv"] = json_obj.get("cv")
        estimator_info["params_type"] = json_obj.get("params_type")
        #
        trained_estimator = _load_estimator(os.path.splitext(filepath)[0] + '.pkl')
        estimator_info["trained_estimator"] = trained_estimator
    #
    return estimator_info

def save_estimator(estimator_info, filepath):
    '''
    '''
    _save_estimator(estimator_info.get("trained_estimator"),
                    os.path.splitext(filepath)[0] + '.pkl')
    estimator_info.pop("trained_estimator")
    #
    with open(filepath, 'w', encoding = "utf8") as fid:
        json.dump(estimator_info, fid)

def read_sklearn_params_from_json(filepath, estimator_name,
                                 params_type = "default"):
    '''
    '''
    params = [{}, {}, {}]
    #
    with open(filepath, encoding = "utf8") as fid:
        json_obj = json.load(fid)
        #
        estimator_obj = json_obj.get(estimator_name).get("parameters")
        if params_type == "default":
            default_params_obj = estimator_obj.get("default parameters")
            if default_params_obj.get("description").strip() == "null":
                pass
            elif default_params_obj.get("description").strip() == "full":
                for param_key in default_params_obj.keys():
                    valid_param_key = param_key.strip()
                    if valid_param_key == "description":
                        pass
                    else:
                        param_obj = default_params_obj.get(param_key)
                        #
                        param_name = param_obj.get("name")
                        params_value = param_obj.get("value")
                        #
                        params[0][param_name] = valid_param_key
                        params[1][param_obj.get("name")] = str(params_value)
                        #
                        if params_value == "None":
                            valid_params_value = None
                        elif params_value == "True":
                            valid_params_value = True
                        elif params_value == "False":
                            valid_params_value = False
                        else:
                            valid_params_value = params_value
                        #
                        params[2][valid_param_key] = valid_params_value
            else:
                pass
        elif params_type == "tuning":
            tuning_params_obj = estimator_obj.get("tuning parameters")
            if tuning_params_obj.get("description").strip() == "null":
                pass
            elif tuning_params_obj.get("description").strip() == "full":
                for param_key in tuning_params_obj.keys():
                    valid_param_key = param_key.strip()
                    if valid_param_key == "description":
                        pass
                    else:
                        param_obj = tuning_params_obj.get(param_key)
                        #
                        param_name = param_obj.get("name")
                        params_value = param_obj.get("value")
                        #
                        params[0][param_name] = valid_param_key
                        # parmas string info for TableWidget
                        params[1][param_obj.get("name")] = ','.join([str(param) for param in params_value]) 
                        #
                        # parmas dict info for sklearn
                        valid_params_value = []
                        for param in params_value:
                            if param == "None":
                                valid_params_value.append(None)
                            elif param == "True":
                                valid_params_value.append(True)
                            elif param == "False":
                                valid_params_value.append(False)
                            else:
                                valid_params_value.append(param)
                        #
                        params[2][valid_param_key] = valid_params_value
            else:
                pass
        elif params_type == "custom":
            pass
        else:
            pass
    #
    return params

if __name__ == "__main__":
    #
    print(load_model(r"C:\Users\lenovo\Desktop\test_sklearn_trainval_test_split\BP.xml"))

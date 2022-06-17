# -*-coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fileIO import RasterImgIO
from data import FeatureProcessor, DataPreprocessor
from util import convert_data_structure

def apply_model_by_img(trained_model, in_file_path, out_file_path, sample_feature, unify_features = False):
    img_info = RasterImgIO.query_geotiff_info(in_file_path)
    tmp_X = RasterImgIO.convert_img_to_2darray(in_file_path)
    if unify_features:
        X, _ = convert_data_structure.dict_to_2darray(FeatureProcessor.unify_feature(tmp_X, sample_feature),
                                                      None)
    X = DataPreprocessor.np_process_invalid_value(X)
    #
    y_prediction = trained_model.predict(X)
    #
    img_width = img_info.get("band_width")
    img_height = img_info.get("band_height")
    crs = img_info.get("crs")
    transform = img_info.get("transform")
    #
    img_arr = RasterImgIO.convert_vector_to_2darray(y_prediction, img_width, img_height)
    RasterImgIO.write_single_band(out_file_path, img_arr, crs, transform)

def test(in_file_path, out_file_path):
    img_info = RasterImgIO.query_geotiff_info(in_file_path)
    tmp_X = RasterImgIO.convert_img_to_2darray(in_file_path)
    img_arr = DataPreprocessor.np_process_invalid_value(tmp_X)
    #
    img_width = img_info.get("band_width")
    img_height = img_info.get("band_height")
    crs = img_info.get("crs")
    transform = img_info.get("transform")
    #
    # img_arr = RasterImgIO.convert_vector_to_2darray(y_prediction, img_width, img_height)
    RasterImgIO.write_geotiff(out_file_path, img_arr, crs, transform)

if __name__ == "__main__":
    #
    test(r"D:\xingrui94\Data\RS_Data\Sentinel3_TOA\S3A_20180605T015441_20180605T015741_Band3-6_ratio.tif",
        r"D:\xingrui94\Data\RS_Data\Sentinel3_TOA\S3A_20180605T015441_20180605T015741_Band3-6_ratio_test.tif")

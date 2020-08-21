import os, sys
sys.path.insert(0, os.path.abspath(".."))

import pandas as pd
import pytest
import pycaret.classification
import pycaret.datasets


def test():
    # loading dataset
    data = pycaret.datasets.get_data('juice')
    assert isinstance(data, pd.core.frame.DataFrame)

    # init setup
    clf1 = pycaret.classification.setup(data, target='Purchase', log_experiment=True, silent=True, html=False, session_id=123)
    assert isinstance(clf1, tuple)
    assert isinstance(clf1[0], pd.core.frame.DataFrame)
    assert isinstance(clf1[1], pd.core.series.Series)
    assert isinstance(clf1[2], pd.core.frame.DataFrame)
    assert isinstance(clf1[3], pd.core.frame.DataFrame)
    assert isinstance(clf1[4], pd.core.series.Series)
    assert isinstance(clf1[5], pd.core.series.Series)
    assert isinstance(clf1[6], int)
    assert isinstance(clf1[8], list)
    assert isinstance(clf1[9], bool)
    assert isinstance(clf1[10], int)
    assert isinstance(clf1[11], bool)
    assert isinstance(clf1[12], list)
    assert isinstance(clf1[13], list)
    assert isinstance(clf1[14], list)
    assert isinstance(clf1[15], str)
    assert isinstance(clf1[16], bool)
    assert isinstance(clf1[17], bool)
    assert isinstance(clf1[18], str)
    assert isinstance(clf1[19], bool)

    # compare models
    top3 = pycaret.classification.compare_models(n_select = 3, exclude=['catboost'])
    assert isinstance(top3, list)

    # tune model
    tuned_top3 = [pycaret.classification.tune_model(i) for i in top3]
    assert isinstance(tuned_top3, list)

    # ensemble model
    bagged_top3 = [pycaret.classification.ensemble_model(i) for i in tuned_top3]
    assert isinstance(bagged_top3, list)

    # blend models
    blender = pycaret.classification.blend_models(top3)

    # stack models
    stacker = pycaret.classification.stack_models(estimator_list = top3)
    predict_holdout = pycaret.classification.predict_model(stacker)

    # select best model
    best = pycaret.classification.automl(optimize = 'MCC')
    
    # hold out predictions
    predict_holdout = pycaret.classification.predict_model(best)
    assert isinstance(predict_holdout, pd.core.frame.DataFrame)

    # predictions on new dataset
    predict_holdout = pycaret.classification.predict_model(best, data=data)
    assert isinstance(predict_holdout, pd.core.frame.DataFrame)

    # calibrate model
    calibrated_best = pycaret.classification.calibrate_model(best)

    # finalize model
    final_best = pycaret.classification.finalize_model(best)

    # save model
    pycaret.classification.save_model(best, 'best_model_23122019')
 
    # load model
    saved_best = pycaret.classification.load_model('best_model_23122019')
    
    # returns table of models
    all_models = pycaret.classification.models()
    assert isinstance(all_models, pd.core.frame.DataFrame)
    
    # get config
    X_train = pycaret.classification.get_config('X_train')
    X_test = pycaret.classification.get_config('X_test')
    y_train = pycaret.classification.get_config('y_train')
    y_test = pycaret.classification.get_config('y_test')
    assert isinstance(X_train, pd.core.frame.DataFrame)
    assert isinstance(X_test, pd.core.frame.DataFrame)
    assert isinstance(y_train, pd.core.series.Series)
    assert isinstance(y_test, pd.core.series.Series)

    # set config
    pycaret.classification.set_config('seed', 124)
    seed = pycaret.classification.get_config('seed')
    assert seed == 124
    
    assert 1 == 1
    
if __name__ == "__main__":
    test()

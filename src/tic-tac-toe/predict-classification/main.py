#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Entry point of the execution in this application.
"""
from datetime import timedelta
from time import monotonic

import pandas as pd
from pandas import DataFrame

from core.chronometer import Chronometer
from core.csv_trials import CsvTrials
from core.graphic_information import GraphicInformation
from core.keras_tuner_hyper import KerasTunerHyper
from core.model_best import ModelBest
from core.model_best_evaluation import ModelBestEvaluation
from core.text_information import TextInformation

if __name__ == '__main__':
    # -------------------------------------------------------------------------
    # Take time from every section.
    # -------------------------------------------------------------------------
    chronometer = Chronometer()
    chronometer.check('Start')

    # -------------------------------------------------------------------------
    # Retrieve data from the CSV file for quick review of the information.
    # -------------------------------------------------------------------------
    data_for_information = pd.read_csv('resources/tic-tac-toe-records-train-reduced-04.csv')

    chronometer.check('Retrieve data information')

    # -------------------------------------------------------------------------
    # Show information in text mode.
    # -------------------------------------------------------------------------
    pandas_information = TextInformation(data_for_information)
    # pandas_information.display_information()
    #
    # chronometer.check('Show information text')

    # -------------------------------------------------------------------------
    # Show information in graphic mode.
    # -------------------------------------------------------------------------
    graphic_information = GraphicInformation(data_for_information, is_show_activated=False)
    columns_by_players_and_cells = ['turn_1_player', 'turn_1_cell',
                                    'turn_5_player', 'turn_5_cell',
                                    'turn_6_player', 'turn_6_cell',
                                    'turn_9_player', 'turn_9_cell',
                                    'winner',
                                    ]
    graphic_information.set_columns(columns_by_players_and_cells)
    # graphic_information.reset_columns()

    # graphic_information.get_distribution_columns()
    # graphic_information.get_correlation_matrix()
    # graphic_information.get_matrix_scatter_plots()
    # graphic_information.get_scatter_plots('turn_1_player', 'turn_1_cell')
    # graphic_information.get_scatter_plots('turn_1_player', 'winner')
    # graphic_information.get_scatter_plots('turn_1_cell', 'winner')
    # graphic_information.get_3d_scatter_plots(
    #     columns=[
    #         ('turn_1_player', 'turn_1_cell', 'winner'),
    #         ('turn_5_player', 'turn_5_cell', 'winner'),
    #         ('turn_6_player', 'turn_6_cell', 'winner'),
    #         ('turn_9_player', 'turn_9_cell', 'winner'),
    #     ],
    #     x_label='Player', y_label='Cell', z_label='Winner'
    # )
    #
    # columns_by_cells = ['turn_1_cell', 'turn_2_cell', 'turn_3_cell', 'turn_4_cell', 'turn_5_cell',
    #                     'turn_6_cell', 'turn_7_cell', 'turn_8_cell', 'turn_9_cell']
    # graphic_information.set_columns(columns_by_cells)
    # graphic_information.get_density(x_label='Cells')
    #
    # columns_by_players = ['winner']
    # graphic_information.set_columns(columns_by_players)
    # graphic_information.get_density(x_label='Winner ID')
    #
    # graphic_information.show()
    #
    # chronometer.check('Show information graph')

    # -------------------------------------------------------------------------
    # Retrieve data from the CSV file for quick review of the deep learning.
    # -------------------------------------------------------------------------
    data_for_train_model = pd.read_csv('resources/tic-tac-toe-records-train-complete.csv')
    # data_for_quick_model = pd.read_csv('resources/tic-tac-toe-records-train-reduced-04.csv')
    data_for_production_model = pd.read_csv('resources/tic-tac-toe-records-production.csv')
    data_for_production_all_model = pd.read_csv('resources/tic-tac-toe-records-production-all.csv')
    data_for_production_one_model = pd.read_csv('resources/tic-tac-toe-records-production-one.csv')
    output_feature = 'winner'

    chronometer.check('Retrieve data')

    # -------------------------------------------------------------------------
    # Create the deep learning model for quick review.
    # -------------------------------------------------------------------------
    # model_quick_review = ModelQuickReview(data_for_quick_model, output_feature)
    # model_quick_review.split_data()
    # model_quick_review.fit()
    # model_quick_review.show_graphic_information()
    # model_quick_review.evaluate()
    #
    # chronometer.check('Model quick review')

    # -------------------------------------------------------------------------
    # Create the deep learning model removing player columns.
    # -------------------------------------------------------------------------
    # player_column_ids = [
    #     'turn_1_player', 'turn_2_player', 'turn_3_player', 'turn_4_player', 'turn_5_player',
    #     'turn_6_player', 'turn_7_player', 'turn_8_player', 'turn_9_player'
    # ]
    # data_without_players = data_for_quick_model.drop(columns=player_column_ids)
    # model_quick_review = ModelQuickReview(data_without_players, output_feature)
    # model_quick_review.split_data()
    # model_quick_review.fit()
    # model_quick_review.show_graphic_information()
    # model_quick_review.evaluate()
    #
    # chronometer.check('Removing player columns')

    # -------------------------------------------------------------------------
    # Create the deep learning model removing cell columns.
    # -------------------------------------------------------------------------
    # player_column_ids = [
    #     'turn_1_cell', 'turn_2_cell', 'turn_3_cell', 'turn_4_cell', 'turn_5_cell',
    #     'turn_6_cell', 'turn_7_cell', 'turn_8_cell', 'turn_9_cell'
    # ]
    # data_without_players = data_for_quick_model.drop(columns=player_column_ids)
    # model_quick_review = ModelQuickReview(data_without_players, output_feature)
    # model_quick_review.split_data()
    # model_quick_review.fit()
    # model_quick_review.show_graphic_information()
    # model_quick_review.evaluate()
    #
    # chronometer.check('Removing cell columns')

    # -------------------------------------------------------------------------
    # Execute the Keras Tuner to search the best of these.
    # -------------------------------------------------------------------------
    player_column_ids = [
        'turn_1_player', 'turn_2_player', 'turn_3_player', 'turn_4_player', 'turn_5_player',
        'turn_6_player', 'turn_7_player', 'turn_8_player', 'turn_9_player'
    ]
    # data_without_players_test: DataFrame = data_for_quick_model.drop(columns=player_column_ids)
    # data_without_players_test: DataFrame = data_for_train_model.drop(columns=player_column_ids)
    #
    # keras_tuner_hyperparameter: KerasTunerHyper = KerasTunerHyper(data_without_players_test,
    #                                                               output_feature, fit_epochs=80)
    # chronometer.check('Keras tuner')
    #
    # keras_tuner_hyperparameter.search()
    # chronometer.check('Keras tuner search')

    # -------------------------------------------------------------------------
    # Store the analysis of the trials in a CSV file.
    # -------------------------------------------------------------------------
    # csv_trials = CsvTrials()
    # csv_trials.generate()
    #
    # chronometer.check('CSV Trials')
    #
    # chronometer.display_information()
    # exit(0)

    # -------------------------------------------------------------------------
    # Fit the best model with the production test data.
    # -------------------------------------------------------------------------
    # trial_id | batch_size | units | layers | learning_rate | epoch | score          | accuracy | crossentropy |
    # -----------------------------------------------------------
    # 11       | 128        | 1024  | 4      | 0.001         | 2     | -0.999999933195326 | 1 | 6.68046737928307E-08 |
    # 19       | 64         | 512   | 4      | 0.001         | 2     | -0.999992905688941 | 1 | 7.09431105860858E-06 |
    # 14       | 512        | 1024  | 4      | 0.001         | 2     | -0.999982224440828 | 1 | 1.77755591721507E-05 |
    # 28       | 128        | 512   | 4      | 0.001         | 1     | -0.999978730855219 | 1 | 2.12691447813995E-05 |
    batch_size: int = 128
    units: int = 1024
    layers: int = 4
    learning_rate: float = 0.001
    ams_grad: bool = False
    epochs: int = 2
    best_model_directory = 'keras-tuner-trials/best-model'
    # data_without_players_production: DataFrame = data_for_train_model.drop(columns=player_column_ids)
    # model_best: ModelBest = ModelBest(data_without_players_production, best_model_directory,
    #                                   output_feature, epochs, batch_size, units, layers,
    #                                   learning_rate, ams_grad)
    # chronometer.check('Best model creation')
    #
    # model_best.fit()
    # chronometer.check('Best model fit')
    #
    # model_best.evaluate()
    # chronometer.check('Best model evaluate')
    #
    # model_best.save()
    # chronometer.check('Best model save')

    # -------------------------------------------------------------------------
    # Evaluate the best model with the test production data.
    # -------------------------------------------------------------------------
    output_categories: int = 3
    data_without_players_production_all: DataFrame = data_for_production_model.drop(columns=player_column_ids)
    model_best_evaluation = ModelBestEvaluation(data_without_players_production_all,
                                                output_feature, best_model_directory,
                                                output_categories)
    chronometer.check('Best model production creation test records')

    model_best_evaluation.evaluate()
    chronometer.check('Best model production evaluation test records')

    # -------------------------------------------------------------------------
    # Evaluate the best model with the all the production data.
    # -------------------------------------------------------------------------
    data_without_players_production_all: DataFrame = data_for_production_all_model.drop(columns=player_column_ids)
    model_best_evaluation = ModelBestEvaluation(data_without_players_production_all,
                                                output_feature, best_model_directory,
                                                output_categories)
    chronometer.check('Best model production creation all records')

    model_best_evaluation.evaluate()
    chronometer.check('Best model production evaluation all records')

    # -------------------------------------------------------------------------
    # Evaluate the best model with the one record of the production data.
    # -------------------------------------------------------------------------
    data_without_players_production_one: DataFrame = data_for_production_one_model.drop(columns=player_column_ids)
    model_best_evaluation = ModelBestEvaluation(data_without_players_production_one,
                                                output_feature, best_model_directory,
                                                output_categories)
    chronometer.check('Best model production creation one record')

    model_best_evaluation.evaluate()
    chronometer.check('Best model production evaluation one record')

    # -------------------------------------------------------------------------
    # Summary of the time line.
    # -------------------------------------------------------------------------
    chronometer.display_information()

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Quick end-to-end check of the deep learning pipeline.

It trains the best model found by the tuner on a CSV of games, saves it, loads it again
and checks the accuracy. It also runs the quick review model and a tiny tuner search.

Usage: python smoke_test.py <games.csv> [--work-dir DIR]
"""
from argparse import ArgumentParser
from os import makedirs
from os.path import join

import pandas as pd

from core.keras_tuner_hyper import KerasTunerHyper
from core.model_best import ModelBest
from core.model_best_evaluation import ModelBestEvaluation
from core.model_quick_review import ModelQuickReview

PLAYER_COLUMNS = [f'turn_{turn}_player' for turn in range(1, 10)]
OUTPUT_FEATURE = 'winner'
OUTPUT_CATEGORIES = 3

if __name__ == '__main__':
    parser = ArgumentParser(description='Train, save, load and evaluate the model on a CSV of games.')
    parser.add_argument('csv_filename', help='CSV created by the game generator.')
    parser.add_argument('--work-dir', default='smoke-test-output',
                        help='Folder for the saved model and the logs.')
    parser.add_argument('--min-accuracy', type=float, default=0.99,
                        help='Fail when the categorical accuracy of the loaded model is lower.')
    args = parser.parse_args()

    makedirs(args.work_dir, exist_ok=True)
    data = pd.read_csv(args.csv_filename).drop(columns=PLAYER_COLUMNS)
    model_path = join(args.work_dir, 'best-model.keras')

    model_best = ModelBest(data, model_path, OUTPUT_FEATURE, epochs=3, batch_size=128, units=256,
                           layers_model=4, learning_rate=0.001, ams_grad=False,
                           tuner_directory=args.work_dir)
    model_best.fit()
    model_best.evaluate()
    model_best.save()

    evaluation = ModelBestEvaluation(data, OUTPUT_FEATURE, model_path, OUTPUT_CATEGORIES).evaluate()
    accuracy = evaluation['categorical_accuracy']
    print(f'Loaded model categorical accuracy: {accuracy:.6f}')
    if accuracy < args.min_accuracy:
        raise SystemExit(f'Accuracy {accuracy:.6f} is lower than {args.min_accuracy}')

    sample = data.sample(n=min(len(data), 20000), random_state=42)

    quick_review = ModelQuickReview(sample, OUTPUT_FEATURE, train_size=0.9)
    quick_review.split_data()
    quick_review.fit()
    quick_review.evaluate()

    tuner = KerasTunerHyper(sample, OUTPUT_FEATURE, fit_epochs=2, train_size=0.9,
                            tuner_directory=join(args.work_dir, 'tuner'))
    tuner.search()
    print('Smoke test passed')

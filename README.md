# Deep Learning

Set of examples and experiments using Deep Learning.

## Tic Tac Toe

“src/tic-tac-toe/”

A deep learning model that learns who won, or whether it was a draw, from the list of turns and moves of a game.

### Game generator

“src/tic-tac-toe/game-generator/” creates the data used to train the model.

```shell
cd src/tic-tac-toe/game-generator
pip install -r requirements.txt
python main.py -n 1000000 -f random-games.csv   # one million random games
python main.py --exhaustive -f all-games.csv    # every possible game, once
behave tests/bdd                                # tests
```

There are 255,168 distinct games of tic-tac-toe:

| Result        | Games   | Share of distinct games | Share of random play |
|---------------|--------:|------------------------:|---------------------:|
| Player 1 wins | 131,184 |                   51.4% |                58.5% |
| Player 2 wins |  77,904 |                   30.5% |                28.8% |
| Draw          |  46,080 |                   18.1% |                12.7% |

### Predict classification

“src/tic-tac-toe/predict-classification/” trains the model with Keras 3 (TensorFlow backend) and uses Keras Tuner to search for the best hyperparameters.

```shell
cd src/tic-tac-toe/predict-classification
pip install -r requirements.txt
python smoke_test.py ../game-generator/all-games.csv   # train, save, load and evaluate
python main.py                                         # full experiment, reads the CSVs in resources/
```

The best configuration found by the tuner (4 dense layers of 1,024 ReLU units, Adam with learning rate 0.001, batch size 128, 2 epochs) reaches 100% accuracy on all 255,168 possible games. An earlier note claimed 99.8%; two things explain the difference:

* One million random games cover about 95% of the distinct games, so most of the "production" games were already in the training data. That set measured memorization more than generalization. The exhaustive generator lets you evaluate on every possible game instead.
* The softmax probability is never exactly 1, so the cross-entropy never reaches 0 even when every game is classified correctly (for example, accuracy 1.0 with a cross-entropy of 6.7e-8).

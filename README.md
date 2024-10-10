# ConscienceCraft: Navigating AI Morality in Text Realms  
**Group Name:** Cyber Sentinels  
**Team Members:**   
1. Sahil Patel 🧑‍💻
2. Nevil Sakhreliya 🧑‍💻
3. Subham Kathiriya 🧑‍💻
4. Sagnick Bhar 🧑‍💻
5. Darshak Devani 🧑‍💻

## Table of Content
  * [Overview](#overview)
  * [Goal](#goal)
  * [Technical Aspect](#technical-aspect)
  * [Technologies Used](#technologies-used)
  * [Results](#results)
  * [Citation](#citation)

## 🌟 Overview  
To develop an evaluation benchmark on the moral ethics of text-based models by analyzing the decisions made by the models in various scenarios which present thousands of diverse and morally significant situations in English and Hindi.  

## 🎯 Motivation and Goal  
In our daily choices, we humans often rely on our conscience, that inner compass that helps us distinguish right from wrong. Unlike us, artificial agents lack this moral sense. This can lead them to unintentionally make morally questionable decisions, especially when they're trained in environments that don't prioritize moral considerations, like certain violent video games. 
As advanced agents learn from various environments, it's crucial to address and minimize any biases they might pick up, especially those that promote immoral behaviour.  
To address this issue, we've developed a project that assesses the moral ethics of text-based models. Our approach involves analyzing decisions made in text-based scenarios which present thousands of diverse and morally significant situations

## 🛠️ Technical Aspect  
Dataset: ETHICS (https://github.com/hendrycks/ethics)

### Algorithm:  
1. Imports:  
The script starts by importing necessary libraries and modules, including os, sys, numpy, argparse, itertools, and torch.utils.data. Additionally, there is a custom utility function load_model and load_process_data loaded from a module named utils.
2. Function Definitions:  
The script defines several functions:
  - main(args): The main function for training and evaluating the model. It loads the model, processes training and test data, and iteratively trains the model for multiple epochs. It records accuracy and exact match metrics.
  - train(model, optimizer, train_dataloader, epoch, log_interval=10): Trains the model for one epoch using the specified dataloader and optimizer.
  - evaluate(model, dataloader): Evaluates the model on a given dataloader and returns accuracy and exact match metrics.
 3. Script Execution:
The script checks if it is the main module and parses command-line arguments using argparse. The arguments control various aspects of the training process, such as model selection, number of GPUs, number of epochs, batch size, learning rate, etc.
4. Training Loop:  
The main training loop involves loading the model, processing data for training and testing, creating data loaders, and training the model for multiple epochs. Evaluation metrics like accuracy and exact match are computed, and the results are logged.
5. Saving Model:  
If the --save flag is provided, the script saves the trained model to a file.


## 💻 Technologies Used 
- Concepts used : BERT-based Model Training and Evaluation, Metrics Calculation (accuracy, AUC), Hyperparameter Tuning.    
- Libraries: os, numpy, pandas, argparse, sklearn.metrics , torch, torch.utils.data, transformers  

## 📚 Citation
ALIGNING AI WITH SHARED HUMAN VALUES (https://arxiv.org/pdf/2008.02275.pdf)  



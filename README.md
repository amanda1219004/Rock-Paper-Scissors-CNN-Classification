# Rock-Paper-Scissor-Computer-Vision
Developed and optimized a Convolutional Neural Network (CNN) to classify Rock, Paper, and Scissors hand gestures, achieving 98.18% test accuracy using TensorFlow and Keras.


## Project Overview

This project focuses on developing a **Computer Vision model using Convolutional Neural Networks (CNN)** to classify hand gestures into three categories: Rock, Paper, and Scissors.

Two CNN architectures were developed and evaluated to identify the best-performing model. The improved CNN achieved **98.18% test accuracy**, demonstrating strong performance in image classification.

## Objectives

- Develop a CNN model to classify Rock, Paper, and Scissors hand gestures.
- Implement image preprocessing techniques.
- Build and compare baseline and improved CNN architectures.
- Evaluate model performance using classification metrics.
- Select and save the best-performing model for future inference and deployment.

## Dataset

**Source:** [Rock Paper Scissors Dataset - Kaggle](https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors)

| Description | Details |
|---|---|
| Total Images | 2,188 |
| Image Format | PNG |
| Original Resolution | 300 × 200 pixels |
| Input Image Size | 150 × 150 pixels |
| Number of Classes | 3 |
| Classes | Rock, Paper, Scissors |

The dataset consists of images representing different hand gestures. Images were resized and normalized before being used for model training.

## Methodology

### 1. Data Preparation

The following preprocessing steps were performed:

- Loading and organizing image data.
- Resizing images to 150 × 150 pixels.
- Normalizing pixel values.
- Preparing training, validation, and testing datasets.
- Encoding image labels for multiclass classification.

### 2. Model Development

Two CNN models were developed and compared.

#### Model 1 - Baseline CNN

The baseline CNN architecture consists of:

- Conv2D layer with 32 filters and ReLU activation.
- MaxPooling2D layer.
- Conv2D layer with 64 filters and ReLU activation.
- MaxPooling2D layer.
- Conv2D layer with 128 filters and ReLU activation.
- MaxPooling2D layer.
- Flatten layer.
- Dense layer with 128 neurons and ReLU activation.
- Dropout layer with a rate of 0.5.
- Dense output layer with 3 neurons and Softmax activation.

The model was compiled using:

- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy
- **Evaluation Metric:** Accuracy

#### Model 2 - Improved CNN

The second CNN model was developed to improve classification performance through architectural modifications.

The improved model contains approximately **4.83 million parameters** and achieved better performance than the baseline CNN.

### 3. Model Evaluation

Both models were evaluated using test accuracy and test loss.

| Model | Test Accuracy | Test Loss |
|---|---:|---:|
| Model 1 - Baseline CNN | 97.57% | 0.1071 |
| Model 2 - Improved CNN | **98.18%** | **0.0696** |

### 4. Model Selection

Based on the evaluation results, **Model 2 was selected as the final model** because it achieved:

- Higher test accuracy.
- Lower test loss.
- Better overall classification performance on the test dataset.

The selected model was saved as:

`rps_model.keras`

## Results and Key Findings

1. Both CNN architectures successfully classified Rock, Paper, and Scissors hand gestures with over 97% test accuracy.
2. The improved CNN achieved **98.18% test accuracy**, outperforming the baseline model by approximately 0.61 percentage points.
3. Test loss decreased from 0.1071 to 0.0696, indicating improved classification performance.
4. The results demonstrate the effectiveness of CNN architectures for multiclass image classification.

## Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Deep Learning | TensorFlow, Keras |
| Data Processing | NumPy |
| Data Visualization | Matplotlib |
| Machine Learning | Convolutional Neural Network (CNN) |
| Development Environment | Google Colab, Jupyter Notebook |
| Model Storage | Keras (.keras) |

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/amanda1219004/Rock-Paper-Scissors-CNN-Classification.git
cd Rock-Paper-Scissors-CNN-Classification
```

### 2. Install Dependencies

```bash
pip install tensorflow numpy matplotlib pillow
```

Install any additional dependencies required by the notebook.

### 3. Download the Dataset

Download the dataset from:

https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors

Extract the dataset and update the directory paths in the notebook if necessary.

### 4. Run the Notebook

Open the project notebook using Jupyter Notebook or Google Colab.

Run all cells sequentially to perform:

1. Data loading and preprocessing.
2. Exploratory data analysis.
3. CNN model development.
4. Model training.
5. Model evaluation and comparison.
6. Model selection and saving.

## Future Improvements

- Implement transfer learning using pretrained models such as MobileNetV2 or EfficientNet.
- Improve model generalization by incorporating more diverse hand gesture images.
- Evaluate performance under different lighting conditions and backgrounds.
- Deploy the trained model using Streamlit.
- Develop real-time hand gesture recognition using webcam input.

## Conclusion

This project demonstrates the implementation of **Deep Learning and Computer Vision** for multiclass image classification.

By developing and comparing two CNN architectures, the improved model achieved **98.18% test accuracy**, outperforming the baseline model.

The project highlights practical experience in image preprocessing, CNN development, model evaluation, and model optimization.

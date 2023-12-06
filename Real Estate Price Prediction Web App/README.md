# Real Estate Price Prediction Web App

## Overview

This project involves creating a web application for predicting real estate prices based on user inputs. The application utilizes a machine learning model, specifically a Ridge Regression model, trained on cleaned real estate data.

## Prerequisites

Ensure you have the necessary Python libraries installed. You can install them using the following:

```bash
pip install pandas scikit-learn Flask
```

## Project Structure

1. **Cleaned_data.csv:** Cleaned dataset used for training the Ridge Regression model.
2. **RidgeModel.pkl:** Serialized Ridge Regression model saved using pickle.
3. **app.py:** Flask application for serving the web interface and making predictions.

## Instructions

1. Run the Flask application using the provided code in `app.py`.
   ```bash
   python app.py
   ```

2. Open your web browser and go to [http://127.0.0.1:5001/](http://127.0.0.1:5001/) to access the application.

3. Choose a location and input the number of bedrooms, bathrooms, and total square footage.

4. Click the "Predict" button, and the application will display the estimated real estate price based on the provided information.

## Web Application

The web application has two main routes:

### 1. Home Page (`/`)

- Displays a form where users can select a location and input the number of bedrooms, bathrooms, and total square footage.

### 2. Prediction Page (`/predict`)

- Accepts form inputs from the home page, processes them, and returns the predicted real estate price.

## Notes

- The machine learning model (`RidgeModel.pkl`) is trained on historical real estate data to predict prices accurately.

- Ensure the required libraries and dependencies are installed before running the application.

- The application runs in debug mode (`debug=True`) to facilitate development. Disable debug mode in a production environment.

- The application listens on port 5001 by default. You can change the port in the `app.run()` statement if needed.


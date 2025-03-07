import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def test_model(model, X_train, y_train, X_test, y_test):
    """
    Trains the given model, makes predictions, and evaluates performance.

    Args:
        model: The ML model to train.
        X_train: Training features.
        y_train: Training labels.
        X_test: Test features.
        y_test: Test labels.
    """
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    print(f"\n{model.__class__.__name__} on Enhanced Features:")
    
    mse = mean_squared_error(y_test, y_pred_test)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred_test)
    r2 = r2_score(y_test, y_pred_test)

    # Store metrics in a dictionary
    model_results = {
        "Model": model.__class__.__name__,
        "Mean Squared Error": mse,
        "Root Mean Squared Error": rmse,
        "Mean Absolute Error": mae,
        "r-squared": r2
    }

    # Convert metrics into DataFrame for readability
    df_metrics = pd.DataFrame([model_results])

    print("\nEvaluation Metrics:")
    print(df_metrics.to_string(index=False))

    return model_results
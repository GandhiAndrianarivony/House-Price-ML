"""Module use for inference"""

def inference(model, data):
    """Make prediction"""

    pred = model.predict(data)
    return pred  # "Prediction [res = inference(model, data)]"

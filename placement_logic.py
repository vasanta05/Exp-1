
def predict_placement(cgpa, aptitude_score, communication_score):
    if (
        cgpa >= 7.0
        and aptitude_score >= 60
        and communication_score >= 60
    ):
        return "PLACED"
    else:
        return "NOT PLACED"


if __name__ == "__main__":
    result = predict_placement(8.0, 75, 80)
    print("Placement Prediction:", result)

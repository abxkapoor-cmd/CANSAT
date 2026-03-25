import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def crop_yield_formula(temperature, humidity, no2_concentration, no3_concentration, visual_assessment_score):
 # Define weightings for different factors
    temperature_weight = 0.002
    humidity_weight = 0.004
    no2_weight = 0.008
    no3_weight = 0.031
    visual_assessment_weight = 0.027

    # Calculate the weighted sum of factors
    weighted_sum = (temperature * temperature_weight +
                    humidity * humidity_weight +
                    no2_concentration * no2_weight +
                    no3_concentration * no3_weight +
                    visual_assessment_score * visual_assessment_weight)

    # Apply the sigmoid function to map the result between 0 and 1
    crop_yield_value = math.log(sigmoid(weighted_sum), 10)

    return crop_yield_value

# Example usage:
temperature_value = 25.5
humidity_value = 52.5
no2_concentration_value = 23.6
no3_concentration_value = 0.04
visual_assessment_score_value = 0.75

yield_result = crop_yield_formula(temperature_value, humidity_value, no2_concentration_value, no3_concentration_value, visual_assessment_score_value)

print("Crop Yield Value:", yield_result)

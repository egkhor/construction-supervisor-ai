import pandas as pd
import numpy as np
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
N_SAMPLES = 500
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "construction_safety_data.csv")

# Feature ranges and categories
WEATHER_CONDITIONS = ['clear', 'rainy', 'foggy', 'hot', 'windy']
EQUIPMENT_STATUSES = ['operational', 'maintenance', 'faulty']
TASK_STATUSES = ['on_track', 'delayed', 'critical']

def generate_safety_features(is_risky: bool) -> dict:
    """Generate synthetic features for construction site safety."""
    worker_count = random.randint(5, 50) if not is_risky else random.randint(20, 100)
    equipment_status = random.choice(EQUIPMENT_STATUSES)
    equipment_faulty = 1 if equipment_status == 'faulty' else 0
    weather = random.choice(WEATHER_CONDITIONS)
    weather_risk = 1 if weather in ['rainy', 'foggy', 'windy'] else 0
    task_status = random.choice(TASK_STATUSES)
    task_delayed = 1 if task_status in ['delayed', 'critical'] else 0
    incident_history = random.randint(0, 3) if not is_risky else random.randint(2, 10)
    hours_worked = random.uniform(4, 10) if not is_risky else random.uniform(8, 16)

    return {
        'worker_count': worker_count,
        'equipment_faulty': equipment_faulty,
        'weather_risk': weather_risk,
        'task_delayed': task_delayed,
        'incident_history': incident_history,
        'hours_worked': hours_worked
    }

def main():
    """Generate synthetic construction safety dataset and save to CSV."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = {
        'worker_count': [],
        'equipment_faulty': [],
        'weather_risk': [],
        'task_delayed': [],
        'incident_history': [],
        'hours_worked': [],
        'is_risky': []
    }

    for _ in range(N_SAMPLES):
        is_risky = random.choice([0, 1])
        features = generate_safety_features(is_risky)
        for key in features:
            data[key].append(features[key])
        data['is_risky'].append(is_risky)

    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Dataset generated and saved to {OUTPUT_FILE}")
    print(df.head())

if __name__ == "__main__":
    main()
# Construction Site Supervisor AI

This open-source project generates synthetic data to train an AI/ML model for construction site safety using Apple's CoreML. The model predicts safety risks based on worker count, equipment status, weather, and more, aiding supervisors in real-time decision-making.

## Features
- **Synthetic Dataset**: 500 samples with features like worker count, equipment faults, weather risks, and task delays.
- **CoreML Compatible**: Ready for CreateML to train tabular classifiers for iOS/macOS apps.
- **Scalable**: Easily adjust dataset size or add new features.

## Project Structure
```
construction-supervisor-ai/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── src/
│   └── generate_safety_data.py
└── data/
    └── construction_safety_data.csv
```

## Getting Started
### Prerequisites
- Python 3.8+
- Xcode 13+ with CreateML
- macOS

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/egkhor/construction-supervisor-ai.git
   cd construction-supervisor-ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate the dataset:
   ```bash
   python src/generate_safety_data.py
   ```
   This creates `data/construction_safety_data.csv`.

### Using with CoreML
1. Open Xcode and create a new CreateML project (Tabular Classifier).
2. Import `data/construction_safety_data.csv`.
3. Set `is_risky` as the target and other columns as features.
4. Train the model and export as a `.mlmodel` for iOS/macOS apps.

## Notes
- **Synthetic Data**: Suitable for prototyping; use real site data for production.
- **Customization**: Increase `N_SAMPLES` in `generate_safety_data.py` for larger datasets.
- **Future Work**: Add features like IoT sensor data or computer vision for enhanced safety monitoring.

## License
MIT License. See [LICENSE](LICENSE) for details.

## Contributing
Contributions welcome! Open issues or submit pull requests on GitHub.

## Contact
Connect via GitHub Issues or LinkedIn: [Your LinkedIn Profile URL]

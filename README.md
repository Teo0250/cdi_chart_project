CDI Rate Project

This repository contains a simple project for fetching and visualizing CDI (Certificado de Depósito Interbancário) rate data. The project consists of two Python scripts: one for data extraction and another for chart generation.
Usage

Data Extraction:
        Run the data extraction script to fetch CDI rate data from the B3 website and save it to a CSV file:

    python cdi_rate_extraction.py

The script will create a file named "taxa-cdi.csv" with the CDI rate data.

Chart Generation:

After running the data extraction script, use the chart generation script to create a line chart of the CDI rates:

    python cdi_rate_chart.py

The chart will be saved as "cdi_chart.png" in the current directory.

Requirements

Make sure you have the required Python packages installed by running:

    pip install -r requirements.txt

License

This project is licensed under the MIT License. Please refer to the LICENSE file for details.

Disclaimer: This project is for educational purposes only and should not be used for financial analysis or decision-making. The CDI rate data obtained from the B3 website may not be accurate or up-to-date. Please consult official financial sources for reliable data and analysis.

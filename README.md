CDI Rate Project

This repository contains a set of scripts for extracting and visualizing CDI (Certificado de Depósito Interbancário) rate data. The project consists of two main Python scripts: one for data extraction and another for chart generation. The data extraction script fetches CDI rate data from the B3 website and saves it to a CSV file. The chart generation script takes the extracted data and creates a line chart to visualize the CDI rate trend over time.
Installation

Clone the repository to your local machine using the following command:

    git clone https://github.com/your-username/cdi_rate_project.git

Install the required Python packages by running:

    pip install -r requirements.txt

Usage

Data Extraction:
        Make sure you have an internet connection as the data extraction script requires it to fetch the CDI rate data.
        Run the data extraction script using the following command:

    python cdi_rate_extraction.py

The script will fetch the CDI rate data, perform some processing, and save the data to a CSV file named "taxa-cdi.csv" in the current directory.

Chart Generation:

After running the data extraction script and obtaining the "taxa-cdi.csv" file, you can generate the CDI rate chart.
    Run the chart generation script using the following command:

    python cdi_rate_chart.py

The script will read the data from "taxa-cdi.csv," create a line chart using the "seaborn" library, and save the chart as "cdi_chart.png" in the current directory.

Contributing

If you would like to contribute to this project, you can follow these steps:

    Fork the repository on GitHub.
    Create a new branch with a descriptive name for your feature or bug fix.
    Make your changes in the new branch.
    Create a pull request to submit your changes for review.

Issues

If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the GitHub repository. We welcome your feedback and contributions to make this project better!
License

This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer: This project is for educational purposes only and should not be used for financial analysis or decision-making. The CDI rate data obtained from the B3 website may not be accurate or up-to-date. Please consult official financial sources for reliable data and analysis.
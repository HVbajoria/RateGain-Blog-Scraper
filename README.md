# RateGain Data Extractor

The Enhanced Blog Data Extractor is a Python-based web scraping tool that allows users to extract comprehensive information from blog pages. This tool has been enhanced with additional features, including multi-language support for translating blog details, integration with Azure Text Analytics for improved translation accuracy, and an improved user interface using Streamlit.

## Key Features

- **Multi-Language Support:**
  Users can choose their preferred language for translating blog titles and dates, enhancing accessibility for users globally.

- **Azure Text Analytics Integration:**
  The tool integrates with Microsoft Azure Text Analytics for accurate and efficient language translation services. This ensures high-quality translation results.

- **Streamlit User Interface:**
  The user interface is built using Streamlit to provide an intuitive and visually appealing experience. The design focuses on user interaction and clarity.

- **Logging System:**
  A robust logging system captures critical information, making it easier to diagnose and troubleshoot potential issues during execution.

## How to Use

1. **Language Selection:**
   - Choose your preferred language for translating blog details from the dropdown menu.

2. **Data Extraction:**
   - Click the "Get Blog Details" button to initiate the data extraction process.
   - A loading spinner is displayed during data fetching and processing.

3. **Download Excel File:**
   - After extraction, download the Excel file containing the blog data.
   - The Excel file includes translated titles, dates, and like counts.

## Dependencies

- **Selenium:** Web automation.
- **BeautifulSoup:** HTML parsing.
- **Streamlit:** Interactive web application.
- **Pandas:** Data manipulation and Excel file creation.
- **Azure Text Analytics:** Language translation.
- **WebDriver Manager:** Web driver management.
- **Openpyxl:** Excel file manipulation.

## Logging

- The application incorporates logging to capture important information and potential errors at the INFO level.

## Configuration

- Ensure the necessary secrets (Azure Translator key and endpoint) are securely stored in Streamlit secrets.

## Deployment

- The application is configured to run in headless mode, suitable for deployment in cloud environments.

## Note

- This tool is designed to extract and analyze blog data, providing an enhanced solution for data extraction and translation.

## Created By:

Name: Harshavardhan Bajoria

College Name: Amity University Kolkata

Graduation Year: 2024

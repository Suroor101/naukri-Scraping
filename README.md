# Job Recommendation System - Web Scraping Script

This is a Python script for web scraping fresher job data from Naukri.com to build a job recommendation system.

## Execution Steps

1. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

2. Download the appropriate ChromeDriver executable for your Chrome browser version and place it in the "data" folder. Make sure to use the correct ChromeDriver version for your browser.

3. Create a virtual environment (optional but recommended) to keep the dependencies isolated:

    ```
    python -m venv venv
    ```

4. Activate the virtual environment (if created):

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

5. Run the main script to start scraping the data:

    ```
    python main.py
    ```

6. The script will start scraping fresher job data from Naukri.com. It will visit pages from 1 to 69 (as per the current configuration). The scraped data will be saved to a CSV file named "scraped_data.csv" inside the "data" folder.

7. Once the script finishes execution, you can find the scraped data in the "data/scraped_data.csv" file.

## Important Notes

- Make sure to have Python installed on your system (Python 3.6 or higher is recommended).
- You may need to update the range of pages in the `start_page` and `end_page` variables in the "main.py" script if Naukri.com changes the number of pages for fresher job listings.
- Ensure that you have an active internet connection to access Naukri.com for scraping the data.
- Please be respectful of the website's terms of service and don't abuse the scraping process.
- The "requirements.txt" file contains the necessary dependencies. Use the given command to install them before running the script.

Happy Scraping!

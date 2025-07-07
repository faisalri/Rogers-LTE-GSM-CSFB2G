# Rogers LTE-GSM CSFB2G Script Generator

Welcome to the **Rogers LTE-GSM CSFB2G Script Generator** web application!
This Streamlit app provides a simple and efficient way to generate configuration scripts for Circuit Switched Fallback (CSFB) from LTE to GSM 2G, based on a customizable template.

## Features

### Script Generation
* **Nodename Input**: Easily enter the specific *nodename* (e.g., `MNCO09XMA`) which will be used in the generated script and as part of the output filename.
* **Cellnames Input**: Provide a list of *cellnames* (e.g., `MNCOXA|MNCOXB|MNCOXC`) separated by `|`. The app will dynamically generate `GeranFreqGroupRelation` entries based on these inputs and determine whether to use `cr` or `crn` based on the internal logic derived from your template example.
* **Dynamic Output Filename**: The generated script will have a filename format like `NODENAME_csfb2G_YYMMDD-HHMM.mos`.
* **Download Option**: After generation, you can preview the script and download it directly as a `.mos` file.

### Template-Based Generation
The core of the script generation relies on an external `template-csfb2G.txt` file, making it flexible and easy to update the underlying configuration logic without changing the app's code.

## How to Run

To run this application on your local machine, follow these steps:

1.  **Clone the repository:**
    If you haven't already, clone this repository to your local machine:
    ```bash
    git clone [https://github.com/YourGitHubUsername/Rogers-LTE-GSM-csfb2G.git](https://github.com/YourGitHubUsername/Rogers-LTE-GSM-csfb2G.git)
    cd Rogers-LTE-GSM-csfb2G
    ```
    (Replace `YourGitHubUsername` with your actual GitHub username.)

2.  **Install Streamlit:**
    Make sure you have Streamlit installed. If not, you can install it via pip:
    ```bash
    pip install streamlit
    ```

3.  **Ensure Template File Exists:**
    Verify that the `template-csfb2G.txt` file is present in the same directory as `app.py`.

4.  **Run the app:**
    Execute the Streamlit application from your terminal:
    ```bash
    streamlit run app.py
    ```
    This command will open the application in your default web browser.

## Contact

Feel free to reach out if you have questions or feedback.

* **Your Name / Company Name**
* [LinkedIn Profile](https://www.linkedin.com/in/faisalriyadi/)
* [GitHub Profile](https://github.com/faisalri)

Thank you for visiting the Rogers LTE-GSM CSFB2G Script Generator! 😊
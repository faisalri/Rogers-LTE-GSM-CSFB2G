import streamlit as st
import datetime
import os

def generate_script(nodename, cellnames_input, template_content):
    """
    Generates the CSFB2G script based on nodename, cellnames, and the template.
    """
    # Replace $nodename and $date placeholders
    current_date = datetime.datetime.now().strftime("%y%m%d-%H%M")
    output_filename = f"{nodename}_csfb2G_{current_date}.mos"
    script_content = template_content.replace(
        "$nodename_csfb2G_$date.log", f"{nodename}_csfb2G_{current_date}.log"
    )

    # Process cellnames
    cell_list = [cell.strip() for cell in cellnames_input.split('|') if cell.strip()]

    if not cell_list:
        st.warning("No valid cellnames were entered. Please provide cellnames separated by '|'.")
        return None, None

    # Section for replacing GeranFreqGroupRelation
    start_marker = "//GeranFreqGroupRelation"
    end_marker_params = "//PARAMTER csfb2G"

    start_index = script_content.find(start_marker)
    end_index = script_content.find(end_marker_params, start_index)

    if start_index == -1 or end_index == -1:
        st.error("Error: Could not find the //GeranFreqGroupRelation block or //PARAMTER csfb2G in the template. Please check the template file structure.")
        return None, None

    # Extract parts before and after the relations block
    # Add a newline after the start_marker to ensure consistent formatting
    before_relations = script_content[:start_index + len(start_marker)]
    after_relations = script_content[end_index:]

    generated_relations = []
    # These are the cells that use 'crn' from the example MNCO09XMA_csfb2G.txt
    cells_using_crn_template = ["MNCOXG", "MNCOXH"]
    
    # Loop through each cellname provided by the user
    for cell in cell_list:
        cell_upper = cell.upper() # Ensure case-insensitive matching
        # Determine whether to use 'crn' or 'cr' based on the template's behavior and your example
        if cell_upper in cells_using_crn_template:
            generated_relations.append(f"crn ENodeBFunction=1,EUtranCellFDD={cell_upper},GeranFreqGroupRelation=GSM850")
        else:
            generated_relations.append(f"cr ENodeBFunction=1,EUtranCellFDD={cell_upper},GeranFreqGroupRelation=GSM850")
        generated_relations.append("GeraNetwork=1,GeranFreqGroup=GSM850")
        generated_relations.append("0\n") # There's an empty line after 0 in the template

    # Combine all parts to form the final script
    # Ensure there's a proper newline structure between sections
    final_script = before_relations + "\n\n" + "\n".join(generated_relations).strip() + "\n\n" + after_relations.strip() + "\n"

    return output_filename, final_script

# --- Streamlit Application ---
st.set_page_config(
    page_title="Rogers LTE-GSM CSFB2G Script Generator",
    layout="centered",
)

st.title("Rogers LTE-GSM CSFB2G Script Generator")

st.markdown(
    """
    This application helps you create CSFB2G (Circuit Switched Fallback 2G) configuration scripts
    for specific nodenames and cellnames.
    """
)

# --- User Input ---

st.header("Input Parameters")

nodename_input = st.text_input(
    "Enter Nodename (e.g., MNCO09XMA):",
    value="",
    placeholder="Example: MNCO09XMA"
)

cellnames_input = st.text_area(
    "Enter Cellnames (separated by '|', e.g., MNCOXA|MNCOXB|MNCOXC):",
    value="",
    height=100,
    placeholder="Example: MNCOXA|MNCOXB|MNCOXC|MNCOXX|MNCOXY|MNCOXZ"
)

# --- Generate Button ---
if st.button("Generate Script"):
    # Basic input validation
    if not nodename_input:
        st.warning("Please enter a Nodename.")
        st.stop() # Stop execution if input is missing
    if not cellnames_input:
        st.warning("Please enter Cellnames.")
        st.stop() # Stop execution if input is missing

    # Define the path to the template file
    template_file_path = os.path.join(os.path.dirname(__file__), "template-csfb2G.txt")

    # Read the template from the file
    try:
        with open(template_file_path, "r") as f:
            template_content = f.read()
    except FileNotFoundError:
        st.error(f"Error: The template file '{template_file_path}' was not found. Please ensure it is in the same directory as this Streamlit application.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred while reading the template file: {e}")
        st.stop()

    # Generate the script
    output_filename, generated_script = generate_script(nodename_input.upper(), cellnames_input.upper(), template_content)

    if generated_script:
        st.success("Script successfully generated!")
        st.subheader(f"Output File: `{output_filename}`")
        st.code(generated_script, language='text', height=400) # Added height for better viewing

        # Download button
        st.download_button(
            label="Download Script",
            data=generated_script,
            file_name=output_filename,
            mime="text/plain"
        )
    else:
        st.error("Script generation failed. Please check the template file structure and your input parameters.")

st.markdown(
    """
    ---
    *Ensure the `template-csfb2G.txt` file is in the same directory as this `app.py` script.*
    """
)
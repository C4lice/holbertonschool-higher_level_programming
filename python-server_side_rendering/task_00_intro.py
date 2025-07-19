
def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        logging.error("Invalid template type. Expected a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid attendees type. Expected a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace placeholders with attendee data or 'N/A' if missing
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            filled_template = filled_template.replace(f"{{{{{key}}}}}", value)

        # Write to output_X.txt
        file_name = f"output_{i}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(filled_template)

def assign_machine(category):

    machine_map = {

        "Label": "Label Printer Line 1",
        "Wristband": "RF Wristband Printer",
        "Tag": "Tag Cutting Machine",
        "Signage": "Large Format Printer"
    }

    return machine_map.get(category, "Manual Review")
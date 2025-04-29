import re

def parse_lab_report_text(text):
    lab_tests = []
    lines = text.split("\n")

    for line in lines:
        match = re.match(r"([\w\s]+)\s+([\d.]+)\s+(\d+[-–]\d+)", line)
        if match:
            test_name = match.group(1).strip()
            test_value = float(match.group(2))
            ref_range = match.group(3).replace("–", "-").split("-")
            ref_low, ref_high = float(ref_range[0]), float(ref_range[1])
            out_of_range = test_value < ref_low or test_value > ref_high

            lab_tests.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": f"{ref_low}-{ref_high}",
                "lab_test_out_of_range": out_of_range
            })

    return lab_tests

import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Simulated reference and current batch data
ref_data = pd.DataFrame({"value": [10, 12, 11, 13, 12, 14]})
curr_data = pd.DataFrame({"value": [11, 13, 12, 14, 15, 13]})

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref_data, current_data=curr_data)
report.save_html("evidently_report.html")
print("Evidently monitoring report generated: evidently_report.html")
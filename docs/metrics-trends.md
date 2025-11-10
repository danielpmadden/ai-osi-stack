© 2025 Daniel P. Madden. Custodial Edition – AI OSI Stack v5.0-open-core.
Unauthorized reproductions or derivatives are not recognized custodial works.
Refer to CANONICAL_PROVENANCE.yaml for official verification.
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Governance Metrics Trends

_Generated at 2025-11-05T10:25:24.414978Z_.

- **PCI**: 100.00%
- **CVR**: 50.00%
- **DDR**: 0.00%
- **AES**: 50.00%
- **BMC**: 100.00%
- **SLGI**: 50.00%

<div id="metrics-trend-chart"></div>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
const history = [{"timestamp": "2025-11-05T10:20:17.298703Z", "values": {"PCI": 0.5, "CVR": 0.5, "DDR": 1.0, "AES": 0.5, "BMC": 1.0, "SLGI": 0.5}}, {"timestamp": "2025-11-05T10:22:40.197881Z", "values": {"PCI": 1.0, "CVR": 0.5, "DDR": 0.0, "AES": 0.5, "BMC": 1.0, "SLGI": 0.5}}, {"timestamp": "2025-11-05T10:25:24.414978Z", "values": {"PCI": 1.0, "CVR": 0.5, "DDR": 0.0, "AES": 0.5, "BMC": 1.0, "SLGI": 0.5}}];
const timestamps = history.map(point => point.timestamp);
const series_pci = {x: timestamps, y: history.map(point => point.values['PCI']), name: 'PCI', mode: 'lines+markers'};
const series_cvr = {x: timestamps, y: history.map(point => point.values['CVR']), name: 'CVR', mode: 'lines+markers'};
const series_ddr = {x: timestamps, y: history.map(point => point.values['DDR']), name: 'DDR', mode: 'lines+markers'};
const series_aes = {x: timestamps, y: history.map(point => point.values['AES']), name: 'AES', mode: 'lines+markers'};
const series_bmc = {x: timestamps, y: history.map(point => point.values['BMC']), name: 'BMC', mode: 'lines+markers'};
const series_slgi = {x: timestamps, y: history.map(point => point.values['SLGI']), name: 'SLGI', mode: 'lines+markers'};
Plotly.newPlot('metrics-trend-chart', [series_pci, series_cvr, series_ddr, series_aes, series_bmc, series_slgi], {title: 'Governance Metric Trends', yaxis: {tickformat: '.0%'}});
</script>
"""Documented real-world events used as ground truth (E2).

Each event: name, category, inclusive date range, and optionally the zones
where the effect is expected (zone-level evaluation). A detection method
"finds" an event when any of its days is ranked within the top-k outliers.

Categories
    disruption : weather / infrastructure events that broke normal operation
    holiday    : calendar effects (expected, recurring)
    artifact   : data/clock artifacts (DST transitions: 23- or 25-hour days)

NOTE: dates were compiled from public records (NOAA, FAA, NYC/MTA, news).
Verify and cite a source for each one before using in the dissertation.
"""

TAXIS_2012 = [
    # disruptions
    {"name": "Hurricane Sandy", "cat": "disruption", "start": "2012-10-29", "end": "2012-10-31",
     "zones": ["132", "138"]},  # JFK, LaGuardia
    {"name": "Post-Sandy recovery (fuel/transit)", "cat": "disruption", "start": "2012-11-01", "end": "2012-11-03"},
    {"name": "Nor'easter Athena", "cat": "disruption", "start": "2012-11-07", "end": "2012-11-07"},
    {"name": "First snowfall of winter", "cat": "disruption", "start": "2012-01-21", "end": "2012-01-21"},
    # holidays
    {"name": "New Year's Day", "cat": "holiday", "start": "2012-01-01", "end": "2012-01-01"},
    {"name": "Memorial Day", "cat": "holiday", "start": "2012-05-28", "end": "2012-05-28"},
    {"name": "Independence Day", "cat": "holiday", "start": "2012-07-04", "end": "2012-07-04"},
    {"name": "Labor Day", "cat": "holiday", "start": "2012-09-03", "end": "2012-09-03"},
    {"name": "Thanksgiving", "cat": "holiday", "start": "2012-11-22", "end": "2012-11-22"},
    {"name": "Christmas Eve/Day", "cat": "holiday", "start": "2012-12-24", "end": "2012-12-25"},
    {"name": "New Year's Eve", "cat": "holiday", "start": "2012-12-31", "end": "2012-12-31"},
    # artifacts
    {"name": "DST start", "cat": "artifact", "start": "2012-03-11", "end": "2012-03-11"},
    {"name": "DST end", "cat": "artifact", "start": "2012-11-04", "end": "2012-11-04"},
]

AIRPORTS_2024 = [
    # disruptions
    {"name": "Midwest winter storms / Chicago snow", "cat": "disruption", "start": "2024-01-12", "end": "2024-01-16",
     "zones": ["ORD", "MDW"]},
    {"name": "Hurricane Beryl (Houston)", "cat": "disruption", "start": "2024-07-08", "end": "2024-07-08",
     "zones": ["IAH", "HOU"]},
    {"name": "CrowdStrike outage / Delta meltdown", "cat": "disruption", "start": "2024-07-19", "end": "2024-07-23",
     "zones": ["ATL", "DTW", "MSP"]},
    {"name": "Hurricane Helene", "cat": "disruption", "start": "2024-09-26", "end": "2024-09-27",
     "zones": ["TPA", "ATL", "CLT"]},
    {"name": "Hurricane Milton", "cat": "disruption", "start": "2024-10-09", "end": "2024-10-10",
     "zones": ["TPA", "MCO"]},
    # holidays
    {"name": "Independence Day", "cat": "holiday", "start": "2024-07-04", "end": "2024-07-04"},
    {"name": "Thanksgiving", "cat": "holiday", "start": "2024-11-28", "end": "2024-11-28"},
    {"name": "Christmas", "cat": "holiday", "start": "2024-12-25", "end": "2024-12-25"},
    # artifacts (flight schedules use local scheduled time: little DST effect expected)
    {"name": "DST start", "cat": "artifact", "start": "2024-03-10", "end": "2024-03-10"},
    {"name": "DST end", "cat": "artifact", "start": "2024-11-03", "end": "2024-11-03"},
]

EVENTS = {"taxis": TAXIS_2012, "airports": AIRPORTS_2024}

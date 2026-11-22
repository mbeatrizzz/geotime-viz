
### taxis — NYC (all zones) — events: all (n=11)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.800 | 0.182 | 0.600 | 0.364 | 0.500 | 0.636 | 0.544 |
| ED (Spatial) | 0.600 | 0.182 | 0.600 | 0.364 | 0.450 | 0.636 | 0.487 |
| Integrated depth (L2) | 0.800 | 0.182 | 0.800 | 0.545 | 0.600 | 0.727 | 0.768 |
| MBD / Func. boxplot | 0.600 | 0.182 | 0.500 | 0.364 | 0.450 | 0.636 | 0.508 |
| Isolation Forest | 0.800 | 0.182 | 0.800 | 0.455 | 0.600 | 0.818 | 0.740 |
| LOF | 0.800 | 0.182 | 0.700 | 0.364 | 0.600 | 0.727 | 0.660 |
| Robust z-score | 0.600 | 0.182 | 0.600 | 0.364 | 0.500 | 0.636 | 0.490 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Christmas Eve/Day | 13 | 15 | 6 | 4 | 11 | 2 | 3 |
| First snowfall of winter | 4 | 3 | 10 | 13 | 16 | 8 | 32 |
| Hurricane Sandy | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| Independence Day | 64 | 78 | 50 | 19 | 59 | 12 | 45 |
| Labor Day | 15 | 14 | 9 | 8 | 18 | 25 | 11 |
| Memorial Day | 28 | 27 | 19 | 11 | 29 | 20 | 20 |
| New Year's Day | 8 | 8 | 4 | 6 | 5 | 7 | 6 |
| New Year's Eve | 76 | 73 | 27 | 71 | 26 | 144 | 128 |
| Nor'easter Athena | 19 | 18 | 22 | 31 | 6 | 174 | 143 |
| Post-Sandy recovery (fuel/transit) | 7 | 9 | 7 | 7 | 8 | 13 | 8 |
| Thanksgiving | 22 | 30 | 15 | 16 | 19 | 28 | 17 |

### taxis — NYC (all zones) — events: disruption (n=4)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.800 | 0.500 | 0.500 | 0.750 | 0.350 | 1.000 | 0.561 |
| ED (Spatial) | 0.600 | 0.500 | 0.500 | 0.750 | 0.300 | 1.000 | 0.493 |
| Integrated depth (L2) | 0.600 | 0.250 | 0.500 | 0.750 | 0.300 | 0.750 | 0.650 |
| MBD / Func. boxplot | 0.400 | 0.250 | 0.300 | 0.500 | 0.250 | 0.750 | 0.377 |
| Isolation Forest | 0.600 | 0.250 | 0.500 | 0.500 | 0.300 | 0.750 | 0.613 |
| LOF | 0.600 | 0.250 | 0.600 | 0.750 | 0.350 | 1.000 | 0.624 |
| Robust z-score | 0.400 | 0.250 | 0.400 | 0.500 | 0.250 | 0.500 | 0.375 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| First snowfall of winter | 4 | 3 | 10 | 13 | 16 | 8 | 32 |
| Hurricane Sandy | 2 | 2 | 1 | 1 | 1 | 1 | 1 |
| Nor'easter Athena | 19 | 18 | 22 | 31 | 6 | 174 | 143 |
| Post-Sandy recovery (fuel/transit) | 7 | 9 | 7 | 7 | 8 | 13 | 8 |

### taxis — NYC (all zones) — events: artifact (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.500 | 0.100 | 0.500 | 0.100 | 1.000 | 0.562 |
| ED (Spatial) | 0.200 | 0.500 | 0.100 | 0.500 | 0.100 | 1.000 | 0.562 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.071 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.035 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.068 |
| LOF | 0.200 | 0.500 | 0.100 | 0.500 | 0.050 | 0.500 | 0.269 |
| Robust z-score | 0.200 | 0.500 | 0.100 | 0.500 | 0.050 | 0.500 | 0.152 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| DST end | 16 | 16 | 17 | 29 | 53 | 41 | 37 |
| DST start | 1 | 1 | 24 | 15 | 2 | 44 | 4 |

### taxis — JFK + LGA — events: all (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.400 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 0.810 |
| ED (Spatial) | 0.400 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 0.810 |
| Integrated depth (L2) | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| MBD / Func. boxplot | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| Isolation Forest | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| LOF | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| Robust z-score | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Sandy | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### taxis — JFK + LGA — events: disruption (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.400 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 0.810 |
| ED (Spatial) | 0.400 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 0.810 |
| Integrated depth (L2) | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| MBD / Func. boxplot | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| Isolation Forest | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| LOF | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |
| Robust z-score | 0.600 | 1.000 | 0.300 | 1.000 | 0.150 | 1.000 | 1.000 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Sandy | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### airports — US (all airports) [delays] — events: all (n=8)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.125 | 0.200 | 0.250 | 0.150 | 0.250 | 0.130 |
| ED (Spatial) | 0.200 | 0.125 | 0.100 | 0.125 | 0.100 | 0.250 | 0.150 |
| Integrated depth (L2) | 1.000 | 0.250 | 0.600 | 0.250 | 0.450 | 0.250 | 0.509 |
| MBD / Func. boxplot | 0.600 | 0.250 | 0.400 | 0.375 | 0.400 | 0.500 | 0.421 |
| Isolation Forest | 1.000 | 0.250 | 0.800 | 0.250 | 0.500 | 0.250 | 0.544 |
| LOF | 0.200 | 0.125 | 0.100 | 0.125 | 0.050 | 0.125 | 0.108 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.059 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Christmas | 277 | 195 | 203 | 140 | 123 | 43 | 115 |
| CrowdStrike outage / Delta meltdown | 3 | 1 | 1 | 1 | 4 | 8 | 32 |
| Hurricane Beryl (Houston) | 156 | 173 | 65 | 56 | 161 | 99 | 97 |
| Hurricane Helene | 105 | 117 | 46 | 46 | 79 | 189 | 106 |
| Hurricane Milton | 191 | 210 | 123 | 106 | 160 | 20 | 215 |
| Independence Day | 358 | 362 | 338 | 289 | 355 | 32 | 351 |
| Midwest winter storms / Chicago snow | 10 | 15 | 2 | 2 | 22 | 1 | 61 |
| Thanksgiving | 245 | 284 | 244 | 108 | 181 | 5 | 278 |

### airports — US (all airports) [delays] — events: disruption (n=5)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.200 | 0.200 | 0.400 | 0.150 | 0.400 | 0.144 |
| ED (Spatial) | 0.200 | 0.200 | 0.100 | 0.200 | 0.100 | 0.400 | 0.168 |
| Integrated depth (L2) | 1.000 | 0.400 | 0.600 | 0.400 | 0.450 | 0.400 | 0.598 |
| MBD / Func. boxplot | 0.400 | 0.200 | 0.300 | 0.400 | 0.350 | 0.600 | 0.374 |
| Isolation Forest | 1.000 | 0.400 | 0.800 | 0.400 | 0.500 | 0.400 | 0.632 |
| LOF | 0.200 | 0.200 | 0.100 | 0.200 | 0.050 | 0.200 | 0.112 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.056 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| CrowdStrike outage / Delta meltdown | 3 | 1 | 1 | 1 | 4 | 8 | 32 |
| Hurricane Beryl (Houston) | 156 | 173 | 65 | 56 | 161 | 99 | 97 |
| Hurricane Helene | 105 | 117 | 46 | 46 | 79 | 189 | 106 |
| Hurricane Milton | 191 | 210 | 123 | 106 | 160 | 20 | 215 |
| Midwest winter storms / Chicago snow | 10 | 15 | 2 | 2 | 22 | 1 | 61 |

### airports — US (all airports) [delays] — events: artifact (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.015 |
| ED (Spatial) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.024 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.044 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.010 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.017 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.020 |
| Robust z-score | 0.000 | 0.000 | 0.100 | 0.500 | 0.050 | 0.500 | 0.069 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| DST end | 258 | 275 | 190 | 210 | 126 | 213 | 147 |
| DST start | 45 | 25 | 13 | 40 | 42 | 102 | 8 |

### airports — US (all airports) [+cancel] — events: all (n=8)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.125 | 0.100 | 0.125 | 0.150 | 0.250 | 0.145 |
| ED (Spatial) | 0.200 | 0.125 | 0.200 | 0.250 | 0.150 | 0.375 | 0.183 |
| Integrated depth (L2) | 1.000 | 0.375 | 0.900 | 0.375 | 0.600 | 0.375 | 0.680 |
| MBD / Func. boxplot | 0.800 | 0.375 | 0.600 | 0.375 | 0.550 | 0.500 | 0.547 |
| Isolation Forest | 1.000 | 0.250 | 0.800 | 0.250 | 0.600 | 0.375 | 0.645 |
| LOF | 0.000 | 0.000 | 0.100 | 0.125 | 0.050 | 0.125 | 0.114 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.060 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Christmas | 289 | 263 | 239 | 165 | 124 | 53 | 115 |
| CrowdStrike outage / Delta meltdown | 3 | 1 | 1 | 1 | 6 | 5 | 32 |
| Hurricane Beryl (Houston) | 126 | 146 | 30 | 33 | 133 | 66 | 96 |
| Hurricane Helene | 94 | 101 | 41 | 39 | 39 | 144 | 108 |
| Hurricane Milton | 32 | 14 | 5 | 18 | 23 | 15 | 192 |
| Independence Day | 356 | 362 | 348 | 276 | 352 | 37 | 356 |
| Midwest winter storms / Chicago snow | 13 | 9 | 2 | 2 | 33 | 1 | 61 |
| Thanksgiving | 272 | 303 | 265 | 128 | 223 | 3 | 291 |

### airports — US (all airports) [+cancel] — events: disruption (n=5)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.200 | 0.100 | 0.200 | 0.150 | 0.400 | 0.163 |
| ED (Spatial) | 0.200 | 0.200 | 0.200 | 0.400 | 0.150 | 0.600 | 0.209 |
| Integrated depth (L2) | 1.000 | 0.600 | 0.900 | 0.600 | 0.600 | 0.600 | 0.803 |
| MBD / Func. boxplot | 0.600 | 0.400 | 0.500 | 0.400 | 0.500 | 0.600 | 0.486 |
| Isolation Forest | 1.000 | 0.400 | 0.800 | 0.400 | 0.600 | 0.600 | 0.755 |
| LOF | 0.000 | 0.000 | 0.100 | 0.200 | 0.050 | 0.200 | 0.120 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.057 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| CrowdStrike outage / Delta meltdown | 3 | 1 | 1 | 1 | 6 | 5 | 32 |
| Hurricane Beryl (Houston) | 126 | 146 | 30 | 33 | 133 | 66 | 96 |
| Hurricane Helene | 94 | 101 | 41 | 39 | 39 | 144 | 108 |
| Hurricane Milton | 32 | 14 | 5 | 18 | 23 | 15 | 192 |
| Midwest winter storms / Chicago snow | 13 | 9 | 2 | 2 | 33 | 1 | 61 |

### airports — US (all airports) [+cancel] — events: artifact (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.034 |
| ED (Spatial) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.041 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.031 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.020 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.042 |
| Robust z-score | 0.000 | 0.000 | 0.100 | 0.500 | 0.050 | 0.500 | 0.070 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| DST end | 52 | 28 | 137 | 149 | 24 | 200 | 141 |
| DST start | 34 | 44 | 21 | 37 | 48 | 139 | 8 |

### airports — ORD [delays] — events: all (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.150 | 1.000 | 0.172 |
| ED (Spatial) | 0.400 | 1.000 | 0.200 | 1.000 | 0.100 | 1.000 | 0.200 |
| Integrated depth (L2) | 0.400 | 1.000 | 0.300 | 1.000 | 0.250 | 1.000 | 0.520 |
| MBD / Func. boxplot | 0.200 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.332 |
| Isolation Forest | 0.400 | 1.000 | 0.400 | 1.000 | 0.250 | 1.000 | 0.637 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.055 |
| Robust z-score | 0.400 | 1.000 | 0.200 | 1.000 | 0.200 | 1.000 | 0.274 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Midwest winter storms / Chicago snow | 3 | 3 | 1 | 1 | 27 | 2 | 3 |

### airports — ORD [delays] — events: disruption (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.150 | 1.000 | 0.172 |
| ED (Spatial) | 0.400 | 1.000 | 0.200 | 1.000 | 0.100 | 1.000 | 0.200 |
| Integrated depth (L2) | 0.400 | 1.000 | 0.300 | 1.000 | 0.250 | 1.000 | 0.520 |
| MBD / Func. boxplot | 0.200 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.332 |
| Isolation Forest | 0.400 | 1.000 | 0.400 | 1.000 | 0.250 | 1.000 | 0.637 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.055 |
| Robust z-score | 0.400 | 1.000 | 0.200 | 1.000 | 0.200 | 1.000 | 0.274 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Midwest winter storms / Chicago snow | 3 | 3 | 1 | 1 | 27 | 2 | 3 |

### airports — ORD [+cancel] — events: all (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.150 | 1.000 | 0.159 |
| ED (Spatial) | 0.200 | 1.000 | 0.100 | 1.000 | 0.150 | 1.000 | 0.315 |
| Integrated depth (L2) | 0.600 | 1.000 | 0.500 | 1.000 | 0.250 | 1.000 | 0.844 |
| MBD / Func. boxplot | 0.400 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.354 |
| Isolation Forest | 0.600 | 1.000 | 0.400 | 1.000 | 0.250 | 1.000 | 0.791 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.048 |
| Robust z-score | 0.400 | 1.000 | 0.200 | 1.000 | 0.200 | 1.000 | 0.276 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Midwest winter storms / Chicago snow | 4 | 1 | 1 | 1 | 26 | 2 | 3 |

### airports — ORD [+cancel] — events: disruption (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.150 | 1.000 | 0.159 |
| ED (Spatial) | 0.200 | 1.000 | 0.100 | 1.000 | 0.150 | 1.000 | 0.315 |
| Integrated depth (L2) | 0.600 | 1.000 | 0.500 | 1.000 | 0.250 | 1.000 | 0.844 |
| MBD / Func. boxplot | 0.400 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.354 |
| Isolation Forest | 0.600 | 1.000 | 0.400 | 1.000 | 0.250 | 1.000 | 0.791 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.048 |
| Robust z-score | 0.400 | 1.000 | 0.200 | 1.000 | 0.200 | 1.000 | 0.276 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Midwest winter storms / Chicago snow | 4 | 1 | 1 | 1 | 26 | 2 | 3 |

### airports — ATL [delays] — events: all (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.500 | 0.200 | 1.000 | 0.150 | 1.000 | 0.154 |
| ED (Spatial) | 0.400 | 0.500 | 0.200 | 0.500 | 0.200 | 1.000 | 0.242 |
| Integrated depth (L2) | 0.800 | 0.500 | 0.500 | 0.500 | 0.250 | 0.500 | 0.535 |
| MBD / Func. boxplot | 1.000 | 0.500 | 0.500 | 0.500 | 0.250 | 0.500 | 0.744 |
| Isolation Forest | 0.800 | 0.500 | 0.500 | 0.500 | 0.300 | 1.000 | 0.561 |
| LOF | 0.200 | 0.500 | 0.100 | 0.500 | 0.050 | 0.500 | 0.098 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.044 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| CrowdStrike outage / Delta meltdown | 9 | 3 | 2 | 2 | 26 | 1 | 94 |
| Hurricane Helene | 5 | 14 | 22 | 14 | 5 | 32 | 14 |

### airports — ATL [delays] — events: disruption (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 0.500 | 0.200 | 1.000 | 0.150 | 1.000 | 0.154 |
| ED (Spatial) | 0.400 | 0.500 | 0.200 | 0.500 | 0.200 | 1.000 | 0.242 |
| Integrated depth (L2) | 0.800 | 0.500 | 0.500 | 0.500 | 0.250 | 0.500 | 0.535 |
| MBD / Func. boxplot | 1.000 | 0.500 | 0.500 | 0.500 | 0.250 | 0.500 | 0.744 |
| Isolation Forest | 0.800 | 0.500 | 0.500 | 0.500 | 0.300 | 1.000 | 0.561 |
| LOF | 0.200 | 0.500 | 0.100 | 0.500 | 0.050 | 0.500 | 0.098 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.044 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| CrowdStrike outage / Delta meltdown | 9 | 3 | 2 | 2 | 26 | 1 | 94 |
| Hurricane Helene | 5 | 14 | 22 | 14 | 5 | 32 | 14 |

### airports — ATL [+cancel] — events: all (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.400 | 1.000 | 0.200 | 1.000 | 0.200 | 1.000 | 0.427 |
| ED (Spatial) | 0.200 | 0.500 | 0.200 | 1.000 | 0.300 | 1.000 | 0.372 |
| Integrated depth (L2) | 0.800 | 0.500 | 0.600 | 1.000 | 0.350 | 1.000 | 0.850 |
| MBD / Func. boxplot | 0.800 | 0.500 | 0.500 | 0.500 | 0.250 | 0.500 | 0.712 |
| Isolation Forest | 0.800 | 0.500 | 0.600 | 1.000 | 0.350 | 1.000 | 0.858 |
| LOF | 0.000 | 0.000 | 0.100 | 0.500 | 0.100 | 1.000 | 0.127 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.055 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| CrowdStrike outage / Delta meltdown | 2 | 1 | 1 | 1 | 15 | 1 | 64 |
| Hurricane Helene | 1 | 10 | 10 | 8 | 8 | 45 | 14 |

### airports — ATL [+cancel] — events: disruption (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.400 | 1.000 | 0.200 | 1.000 | 0.200 | 1.000 | 0.427 |
| ED (Spatial) | 0.200 | 0.500 | 0.200 | 1.000 | 0.300 | 1.000 | 0.372 |
| Integrated depth (L2) | 0.800 | 0.500 | 0.600 | 1.000 | 0.350 | 1.000 | 0.850 |
| MBD / Func. boxplot | 0.800 | 0.500 | 0.500 | 0.500 | 0.250 | 0.500 | 0.712 |
| Isolation Forest | 0.800 | 0.500 | 0.600 | 1.000 | 0.350 | 1.000 | 0.858 |
| LOF | 0.000 | 0.000 | 0.100 | 0.500 | 0.100 | 1.000 | 0.127 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.055 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| CrowdStrike outage / Delta meltdown | 2 | 1 | 1 | 1 | 15 | 1 | 64 |
| Hurricane Helene | 1 | 10 | 10 | 8 | 8 | 45 | 14 |

### airports — TPA [delays] — events: all (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.010 |
| ED (Spatial) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.066 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.010 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.012 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.007 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Helene | 62 | 90 | 87 | 59 | 42 | 24 | 220 |
| Hurricane Milton | 365 | 362 | 361 | 364 | 353 | 25 | 363 |

### airports — TPA [delays] — events: disruption (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.010 |
| ED (Spatial) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.066 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.010 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.012 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.007 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Helene | 62 | 90 | 87 | 59 | 42 | 24 | 220 |
| Hurricane Milton | 365 | 362 | 361 | 364 | 353 | 25 | 363 |

### airports — TPA [+cancel] — events: all (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 |
| ED (Spatial) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.042 |
| Integrated depth (L2) | 0.600 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.812 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 |
| Isolation Forest | 0.600 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.551 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.098 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.012 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Helene | 45 | 57 | 1 | 2 | 16 | 22 | 185 |
| Hurricane Milton | 46 | 58 | 2 | 3 | 27 | 23 | 204 |

### airports — TPA [+cancel] — events: disruption (n=2)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 |
| ED (Spatial) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.042 |
| Integrated depth (L2) | 0.600 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.812 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.071 |
| Isolation Forest | 0.600 | 1.000 | 0.300 | 1.000 | 0.200 | 1.000 | 0.551 |
| LOF | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.500 | 0.098 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.012 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Helene | 45 | 57 | 1 | 2 | 16 | 22 | 185 |
| Hurricane Milton | 46 | 58 | 2 | 3 | 27 | 23 | 204 |

### airports — IAH + HOU [delays] — events: all (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.167 |
| ED (Spatial) | 0.000 | 0.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.111 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.024 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.031 |
| LOF | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.250 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.040 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Beryl (Houston) | 6 | 9 | 110 | 32 | 4 | 42 | 25 |

### airports — IAH + HOU [delays] — events: disruption (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.000 | 0.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.167 |
| ED (Spatial) | 0.000 | 0.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.111 |
| Integrated depth (L2) | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.009 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.024 |
| Isolation Forest | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.031 |
| LOF | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.250 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.040 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Beryl (Houston) | 6 | 9 | 110 | 32 | 4 | 42 | 25 |

### airports — IAH + HOU [+cancel] — events: all (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.333 |
| ED (Spatial) | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 1.000 |
| Integrated depth (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 1.000 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.032 |
| Isolation Forest | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 1.000 |
| LOF | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.333 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.043 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Beryl (Houston) | 3 | 1 | 1 | 1 | 3 | 31 | 23 |

### airports — IAH + HOU [+cancel] — events: disruption (n=1)

| method | P@5 | EvR@5 | P@10 | EvR@10 | P@20 | EvR@20 | AP |
|---|---|---|---|---|---|---|---|
| ED (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.333 |
| ED (Spatial) | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 1.000 |
| Integrated depth (L2) | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 1.000 |
| MBD / Func. boxplot | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.032 |
| Isolation Forest | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 1.000 |
| LOF | 0.200 | 1.000 | 0.100 | 1.000 | 0.050 | 1.000 | 0.333 |
| Robust z-score | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.043 |

Best rank of each event (1 = most outlying day):

| event | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| Hurricane Beryl (Houston) | 3 | 1 | 1 | 1 | 3 | 31 | 23 |

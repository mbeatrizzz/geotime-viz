Reference: ED with L2 depth, r = 100 levels, hourly (P=24), all variables, full day.

| scenario | variation | kendall_tau | top10_overlap |
|---|---|---|---|
| taxis / NYC (all zones) | Spatial depth | 0.856 | 0.900 |
| taxis / NYC (all zones) | r = 20 levels | 0.847 | 0.900 |
| taxis / NYC (all zones) | r = 10 levels | 0.713 | 0.700 |
| taxis / NYC (all zones) | 2-hour bins (P=12) | 0.850 | 0.900 |
| taxis / NYC (all zones) | 4-hour bins (P=6) | 0.795 | 0.900 |
| taxis / NYC (all zones) | Hours 06-23 only | 0.767 | 0.700 |
| taxis / NYC (all zones) | Without 'count' | 0.778 | 0.800 |
| taxis / NYC (all zones) | Without 'duration' | 0.710 | 0.600 |
| taxis / NYC (all zones) | Without 'trip_distance' | 0.731 | 0.900 |
| taxis / NYC (all zones) | Without 'fare_amount' | 0.817 | 0.900 |
| taxis / NYC (all zones) | Integrated depth (no ED ordering) | 0.675 | 0.600 |
| airports / US (all airports) +cancel | Spatial depth | 0.757 | 0.700 |
| airports / US (all airports) +cancel | r = 20 levels | 0.872 | 0.400 |
| airports / US (all airports) +cancel | r = 10 levels | 0.775 | 0.300 |
| airports / US (all airports) +cancel | 2-hour bins (P=12) | 0.790 | 0.700 |
| airports / US (all airports) +cancel | 4-hour bins (P=6) | 0.699 | 0.600 |
| airports / US (all airports) +cancel | Hours 06-23 only | 0.714 | 0.200 |
| airports / US (all airports) +cancel | Without 'DepDelay' | 0.845 | 0.900 |
| airports / US (all airports) +cancel | Without 'CarrierDelay' | 0.851 | 0.900 |
| airports / US (all airports) +cancel | Without 'WeatherDelay' | 0.809 | 0.500 |
| airports / US (all airports) +cancel | Without 'SecurityDelay' | 0.644 | 0.900 |
| airports / US (all airports) +cancel | Without 'Cancelled' | 0.867 | 0.700 |
| airports / US (all airports) +cancel | Integrated depth (no ED ordering) | 0.505 | 0.100 |
| airports / ORD +cancel | Spatial depth | 0.805 | 0.800 |
| airports / ORD +cancel | r = 20 levels | 0.895 | 0.400 |
| airports / ORD +cancel | r = 10 levels | 0.801 | 0.200 |
| airports / ORD +cancel | 2-hour bins (P=12) | 0.782 | 0.500 |
| airports / ORD +cancel | 4-hour bins (P=6) | 0.665 | 0.400 |
| airports / ORD +cancel | Hours 06-23 only | 0.914 | 0.700 |
| airports / ORD +cancel | Without 'DepDelay' | 0.846 | 1.000 |
| airports / ORD +cancel | Without 'CarrierDelay' | 0.801 | 0.900 |
| airports / ORD +cancel | Without 'WeatherDelay' | 0.881 | 0.700 |
| airports / ORD +cancel | Without 'SecurityDelay' | 0.744 | 0.600 |
| airports / ORD +cancel | Without 'Cancelled' | 0.911 | 0.900 |
| airports / ORD +cancel | Integrated depth (no ED ordering) | 0.566 | 0.200 |

N=300, P=24, V=3, contamination=3%, 10 seeds. k = number of injected anomalies.

### Average precision

| type | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| amplitude | 0.287 | 0.212 | 0.126 | 0.577 | 0.956 | 0.386 | 0.614 |
| collapse | 1.000 | 0.737 | 1.000 | 0.995 | 1.000 | 1.000 | 1.000 |
| magnitude_isolated | 0.996 | 0.996 | 0.170 | 0.473 | 1.000 | 0.057 | 0.469 |
| magnitude_persistent | 0.771 | 0.759 | 0.989 | 0.973 | 0.961 | 0.967 | 0.975 |
| shape_phase | 0.964 | 0.948 | 0.991 | 0.993 | 1.000 | 0.743 | 0.992 |
| single_variable | 1.000 | 1.000 | 1.000 | 0.978 | 1.000 | 0.149 | 0.895 |
| mean | 0.836 | 0.775 | 0.713 | 0.831 | 0.986 | 0.550 | 0.824 |

### Precision@k (k = #anomalies)

| type | ED (L2) | ED (Spatial) | Integrated depth (L2) | Isolation Forest | LOF | MBD / Func. boxplot | Robust z-score |
|---|---|---|---|---|---|---|---|
| amplitude | 0.300 | 0.222 | 0.078 | 0.500 | 0.967 | 0.289 | 0.556 |
| collapse | 1.000 | 0.667 | 1.000 | 0.989 | 1.000 | 1.000 | 1.000 |
| magnitude_isolated | 0.989 | 0.989 | 0.167 | 0.456 | 1.000 | 0.044 | 0.456 |
| magnitude_persistent | 0.678 | 0.667 | 0.956 | 0.911 | 0.889 | 0.900 | 0.911 |
| shape_phase | 0.911 | 0.878 | 0.944 | 0.956 | 1.000 | 0.756 | 0.967 |
| single_variable | 1.000 | 1.000 | 1.000 | 0.922 | 1.000 | 0.144 | 0.822 |
| mean | 0.813 | 0.737 | 0.691 | 0.789 | 0.976 | 0.522 | 0.785 |

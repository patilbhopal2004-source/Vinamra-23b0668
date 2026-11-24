# Delhi Yamuna DO-BOD study (CE 766 project)

Evaluating interventions for dissolved-oxygen (DO) recovery in the Delhi stretch of the Yamuna River (Wazirabad to Okhla), January 2023 to March 2026.

## Contents
- `data/yamuna_observed_data.csv` : four tables typed in from the sources below (station water quality on two dates, drain shares of discharge and BOD load, monthly drain BOD compliance). DO reported as NIL is stored as 0 in the code.
- `code/analysis.py` : computes station distances from coordinates, drain contribution statistics, and produces the figure.
- `figures/fig1_observed_data.png` : Fig. 1 of the preliminary submission.

Run: `pip install numpy matplotlib` then `python code/analysis.py` from the repo root.

## Original data sources
1. Delhi Pollution Control Committee (DPCC). Water Quality Status of River Yamuna, report of sampling dated 09.03.2026 (DPCC/W/Y/2026/17-24). https://dpcc.delhi.gov.in/sites/default/files/DPCC/analysis-report/river_yamuna_march-26%29_1%29.pdf
2. DPCC. Water Quality Status of River Yamuna, report of sampling dated 01.05.2025 (DPCC/W/Y/2025/09-16). https://dpcc.delhi.gov.in/sites/default/files/DPCC/analysis-report/d2146c3980414253b33afa98c24efb24.pdf
3. Department of Environment, Govt. of NCT of Delhi (2025). Yamuna of NCT of Delhi: Water Quality Monitoring by DPCC (Yamuna book, April 2025). https://environment.delhi.gov.in/sites/default/files/environment/universal/v2.0_final_yamuna_book_april_2025_compressed_2.pdf



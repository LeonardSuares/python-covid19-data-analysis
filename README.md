# Covid-19 Global Intelligence Dashboard

An interactive platform built with **Streamlit** and **Plotly** to visualize pandemic trends and recovery efficiency. This project utilizes the Worldometer and WHO datasets to provide a multi-faceted view of the global response.

---

## Key Features

* **Regional Recovery Comparison:** A dynamic benchmarking tool to identify which WHO Regions (Europe, Americas, etc.) have the highest recovery-to-case ratios.
* **Interactive Treemaps:** Visual hierarchy of the top 20 countries by Total Cases, Deaths, and Active infections.
* **Country-Level Deep Dive:** Searchable time-series analysis for individual countries, comparing Confirmed vs. Recovered trends.
* **Metric Switcher Prompts:** User-driven charts that toggle between Recovery Rates and Mortality Rates using Streamlit's reactive widgets.
* **Optimized Data Pipeline:** Centralized processing in `utils.py` with `@st.cache_data` to handle high-volume CSV files efficiently.

---

## Tech Stack

* **Language:** `Python 3.x`
* **Data Science:** `Pandas`, `NumPy`
* **Visuals:** `Plotly Express`, `Plotly Graph Objects`
* **UI/UX:** `Streamlit` (Multi-page Architecture)

---

## 📂 Project Architecture

```text
Covid-Analysis/
├── Home.py               # Landing page & Global Trend Line
├── utils.py              # Centralized ETL & Date handling
├── data/                 # Dataset storage
│   ├── worldometer_data.csv
│   ├── full_grouped.csv
│   └── day_wise.csv
└── pages/
    ├── 1_Regional_Analysis.py   # Treemaps & Regional Recovery Comparisons
    ├── 2_Ratios_and_Rankings.py # Sorting countries by test/death ratios
    └── 3_Country_Deep_Dive.py   # Specific country time-series lookup

# Creator Campaign Dashboard

A Streamlit-based dashboard to manage creator campaigns more efficiently using a structured workflow and basic AI-assisted features.

---

## Problem

The existing workflow relies on Google Sheets, which:
- Contains unstructured and inconsistent data  
- Makes filtering creators slow and manual  
- Lacks support for decision-making  

---

## Solution

This project converts the raw creator dataset into a simple dashboard where users can:
- Create and manage campaigns  
- Filter creators based on niches  
- Evaluate creators using key metrics  
- Classify creators for campaign selection  

---

## Features

### Campaign Management
- Create new campaigns with code and name  
- Select target niches  
- View and select existing campaigns  

---

### Creator Filtering
- Filters creators based on selected niches  
- Uses both primary and secondary niches for matching  

---

### Creator Classification
- Mark creators as shortlisted, backup, or rejected  

---

### AI-Assisted Features
- Relevance scoring based on engagement, reach, and views  
- Basic recommendation system for top creators  
- Detection of incomplete profiles  

---

### Campaign Summary
- Shows number of shortlisted, backup, and rejected creators  
- Provides a quick overview of campaign status  

---

## Tech Stack

- Python  
- Streamlit  
- Pandas  

---

## Project Structure
├── app.py
├── components/
├── utils/
├── data/
├── styles.py
├── requirements.txt


---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

# 📱 Google Play Store App Market Analysis

This project is a comprehensive data analysis of the Android app market using data scraped from the Google Play Store. We explore various aspects like app ratings, size, price, revenue, installs, and categories to uncover insights into the app ecosystem.

---

## 📂 Dataset Information

**Source:**  
The dataset was collected by **Lavanya Gupta** in 2018 through web scraping.  
It contains information about **10,000+ apps**, including their metadata and user reviews.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Plotly Express**
- **Jupyter Notebook**

---

## 🧹 Data Cleaning Steps

- Dropped unused columns (`Last_Updated`, `Android_Ver`)
- Removed rows with missing ratings
- Dropped duplicate entries
- Converted data types for `Installs` and `Price`
- Removed outliers (apps priced above $250)

---

## 📊 Exploratory Data Analysis

### ⭐ Highest Rated App

- `KBA-EZ Health Guide` with a perfect 5.0 rating  
  ⚠️ Only 4 reviews — highlights the **problem with low review counts** skewing results.

### 📦 Largest Apps (by size)

- Top apps were around **100 MB**, possibly suggesting a size limit or developer preference.

### 📝 Most Reviewed Apps

- `Facebook`, `WhatsApp`, `Instagram`, and `Messenger` topped the list — all **free apps**.

### 🧒 Content Ratings Distribution

- Majority rated `Everyone`, followed by `Teen` and `Mature 17+`.

### 📥 Installs Breakdown

- 20 apps had **1 Billion+ installs**
- 3 apps had **only 1 install**

---

## 💸 Price & Revenue Analysis

### 💰 Most Expensive Apps (After Cleaning)

- `Vargo Anesthesia Mega App` — $79.99
- Many "I'm Rich" style novelty apps were removed

### 📈 Revenue Estimation

Added a new column `Revenue_Estimate = Installs × Price`

**Top Grossing Paid Apps:**

1. `Minecraft` - Estimated ~$69.9 million
2. `Hitman Sniper` - ~$9.9 million
3. `GTA: San Andreas` - ~$6.9 million  
   🎮 **Games dominate** the top 10 in revenue

---

## 📐 Visual Insights with Plotly

### 📎 Category Trends

- **Most Competitive Categories:** `FAMILY`, `GAME`, `TOOLS`
- **Most Downloaded Categories:** `COMMUNICATION`, `SOCIAL`, `VIDEO_PLAYERS`

### 📊 Genre Breakdown

- 114 unique genre entries (after cleaning nested values)
- Top genre: `Tools`

### 🆚 Free vs Paid Apps per Category

- Vast majority of apps are **Free**
- Very few **Paid apps** in most categories

### 📉 Paid App Challenges

- Paid apps have **significantly fewer installs**
- Free apps dominate in reach and usage

---

## 📈 Revenue by Category

- Most paid apps **do not** recoup a $30,000 development cost
- Median revenue varies widely by category

---

## 💵 Pricing Strategy

- **Median paid app price:** `$2.99`
- Some categories (e.g., `MEDICAL`) have **much higher price variance**

---

## 📌 Key Takeaways

- **Free apps dominate** in downloads and number.
- **Ratings alone are not reliable** — must consider number of reviews.
- **Revenue is concentrated** in top-performing apps, mainly games.
- **Paid apps struggle** with visibility and reach compared to free ones.

---

```plaintext
      |\__/,|   (`\
    _.|o o  |_   ) )
  -(((---(((--------

Hi, this is me playing around with some geospatial data 🗺️
```

---

## 📦 Project Setup

### 🐍 1. Install Python

Make sure you're using **Python 3.11.9**.

---

### 📁 2. Folder Structure

You'll need the following folders in the root directory:

```
/project-root
│
├── data/
├── dashboard/
├── assets/
├── Flask/
├── .env
├── citypopulation_webscraper.ipynb
├── EDA.ipynb
├── map_maker.ipynb
```

---

### 📄 3. Required Files

Inside the `data/` folder, place these files:

- `data.xlsx` — export from Contactous
- `population.xlsx` — updated from [citypopulation.de](https://www.citypopulation.de)
- `multiplier.xlsx` — ask for this file if you don’t have it
- `a file for Arfica SA`*****  —  We shall see if we get the file

---

### 🔐 4. Environment Variables

Create a `.env` file in the root folder with the following entries:

```env
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
GCLOUD_KEY=your_google_cloud_api_key
```

GCLOUD_KEY is NOT needed for map_maker.ipynb

#### 🔑 How to get them:

- **GOOGLE_MAPS_API_KEY**:  
  Follow this guide → [Get a Maps JavaScript API Key](https://developers.google.com/maps/documentation/javascript/get-api-key)

- **GCLOUD_KEY**:  
  Create a Google Cloud Project → enable the **GMaps API** → generate your API key.

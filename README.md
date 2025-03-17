# Renovation-LLM – AI-Powered Interior Design Assistant  

**An AI-powered tool that assists interior designers and architects by analyzing real-world renovation datasets and generating high-quality design visuals based on user prompts.**  

## 📌 Overview  
Renovation-LLM is a **workflow-driven AI assistant** that helps interior designers and architects streamline their creative process. This project is a small-scale version of what **Renovate.ai** does, utilizing **structured interior design data** and **AI-powered image generation** to offer personalized design inspiration.  

The tool **analyzes a large dataset of interior design images**, extracts structured insights, and generates SQL queries based on user prompts. It then **retrieves relevant design data** and feeds it into OpenAI’s image generation models to create stunning AI-powered interior design concepts.  

## 🔥 Key Features  
✅ **Interior Design Data Analysis** – Processes **real-world renovation datasets** from Kaggle.  
✅ **PostgreSQL Storage** – Stores structured image metadata for **efficient querying and retrieval**.  
✅ **AI-Powered Workflow** – Uses an **agentic framework** to process prompts and generate SQL queries dynamically.  
✅ **Keyword Extraction** – Extracts key **design elements** from user inputs to retrieve the most relevant images.  
✅ **AI Image Generation** – Uses **OpenAI’s image generator** to create custom design concepts based on structured data.  

## 🏗️ Tech Stack  
- **Database:** PostgreSQL (Stores interior design image metadata)  
- **Data Processing:** Python (for dataset processing and SQL integration)  
- **AI Agent Framework:** Custom workflow for function calling & query generation  
- **Image Generation:** OpenAI API (Generates new interior design concepts)  
- **Dataset Source:** Kaggle (Synthetic Home Interior Dataset)  

## 📂 Dataset & Processing  
The dataset was downloaded from **Kaggle**:  
```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("luznoc/synthetic-dataset-for-home-interior")
```
Each image was analyzed and stored in a **PostgreSQL database** with the following schema:  
| Column Name       | Data Type  | Description |
|------------------|-----------|-------------|
| id              | INT (PK)  | Unique identifier for each image |
| image_url       | TEXT      | Link to the original image |
| image_description | TEXT      | AI-generated description of the image |
| room_type       | TEXT      | Type of room (e.g., kitchen, living room) |
| price           | FLOAT     | Estimated renovation cost |
| color          | TEXT      | Primary colors in the image |
| style         | TEXT      | Design style (e.g., modern, vintage) |

## 🛠️ Installation & Setup  
### **Clone the repository:**  
```sh
git clone https://github.com/MozartofCode/Renovation-LLM.git
cd Renovation-LLM
```

### **Set up the PostgreSQL database**  
1. Install PostgreSQL and create a database:  
   ```sql
   CREATE DATABASE renovation_db;
   ```
2. Set up the table schema:  
   ```sql
   CREATE TABLE renovation_photos (
       id SERIAL PRIMARY KEY,
       image_url TEXT,
       image_description TEXT,
       room_type TEXT,
       price INT,
       color TEXT,
       style TEXT
   );
   ```
3. Load the dataset into PostgreSQL using a Python script (provided in the repo).  

## 🎯 How It Works  
1️⃣ **User enters a design prompt** (e.g., "modern kitchen with white marble countertops").  
2️⃣ The AI **extracts key design elements** (e.g., "modern", "kitchen", "marble").  
3️⃣ It **generates an SQL query** to retrieve **matching images from the database**.  
4️⃣ The **retrieved image descriptions** are **fed into OpenAI’s image generator** to create a high-quality **AI-generated design**.  

## 🚧 Future Enhancements  
🔹 **Integration with 3D Rendering Software** – Connect with **Blender or Unreal Engine** for realistic renderings.  
🔹 **User Preference Learning** – Train AI models to recommend designs based on past preferences.  
🔹 **Multi-Modal AI** – Combine **text, image, and video** for richer design recommendations.  


## 📬 Contact  
**Author:** Bertan Berker  
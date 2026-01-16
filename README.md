🖼️ Image Scraper Flask App

A simple yet powerful Flask web application that allows users to search for images from Google, download them locally, and store them in MongoDB Atlas.
This project demonstrates web scraping, Flask-based web development.

🚀 Features

🌐 Search any keyword and scrape images from Google.

💾 Automatically saves images into a local folder (images/).

🧱 Built with Flask for a simple, interactive web interface.

📜 Includes error handling and logging (image_scrapper_log file).

🧩 Tech Stack
Component	Technology Used
Backend	Python (Flask)
Scraping	BeautifulSoup, Requests
Frontend	HTML, CSS (via templates/index.html)
Logging	Python Logging Module
📁 Project Structure
ImageScraper/
│
├── templates/
│   └── index.html        # Frontend UI for search form
│
├── images/               # Saved scraped images (auto-created)
│
├── app.py                # Main Flask application file
│
├── requirements.txt      # All required dependencies
│
├── image_scrapper_log    # Log file for debugging
│
└── README.md             # Project documentation

⚙️ Installation and Setup
1️⃣ Clone this repository
git clone https://github.com/<your-username>/ImageScraper.git
cd ImageScraper

2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate  # For Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Flask application
python app.py

5️⃣ Open in browser

Visit → http://127.0.0.1:5000/
Enter a keyword and hit Search to start scraping images!


🧠 How It Works

User enters a keyword (e.g., cats) on the homepage.

Flask sends a request to Google Images.

BeautifulSoup scrapes the image URLs.

The app downloads and saves them locally in the images/ folder.


🪵 Logging

Any exceptions or events are recorded in:

image_scrapper_log


This helps track scraping errors or connection issues.

🧾 Example Usage

Input:

dogs


Output:

Images of dogs saved in /images/

🧑‍💻 Author

Developed by: sushil
GitHub: https://github.com/sknn997
Tech: Python | Flask | BeautifulSoup |

📜 License

This project is open-source under the MIT License.
Feel free to modify and use it for learning or personal projects.

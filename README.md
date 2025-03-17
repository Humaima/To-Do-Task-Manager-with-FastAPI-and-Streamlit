# To-Do Task Manager with FastAPI and Streamlit

🚀 **A fully functional To-Do Task Manager built with FastAPI (backend) and Streamlit (frontend).**

This project demonstrates how to build a **CRUD (Create, Read, Update, Delete)** application using modern Python frameworks. The backend is powered by **FastAPI**, while the frontend is built with **Streamlit** for an interactive user experience. The application uses **SQLite** for database storage and **SQLAlchemy** for database management.

## Features

- **CRUD Operations**:
  - Create, read, update, and delete tasks effortlessly.
- **FastAPI Backend**:
  - RESTful API with endpoints for managing tasks.
  - Automatic Swagger UI documentation.
  ![image](https://github.com/user-attachments/assets/89525e7d-971b-445f-a465-8df6b22d2273)
- **Streamlit Frontend**:
  - Interactive and user-friendly interface.
  - Create, update, and delete tasks directly from the UI.
  ![image](https://github.com/user-attachments/assets/5423f55c-4b9a-412d-abd1-1a6cc401feae)
![image](https://github.com/user-attachments/assets/0e676d62-d291-4a2e-90ec-4ad673f7b2b4)
- **Database Integration**:
  - SQLite database for lightweight and efficient data storage.
  - SQLAlchemy for ORM-based database management.
  ![image](https://github.com/user-attachments/assets/30445292-4fe1-4add-bea1-5efcd82976a7)
- **Authentication**:
  - API key authentication for secure access to the backend.

---

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Authentication**: API Key

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Humaima/To-Do-Task-Manager-with-FastAPI-and-Streamlit
   cd your-repo-name

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the FastAPI backend**
   ```bash
   uvicorn main:app --reload
   Access the FastAPI Swagger UI at http://127.0.0.1:8000/docs.
5. **Run the Streamlit frontend**
    ```bash
    streamlit run streamlit.py
## License
This project is licensed under the MIT License. See the LICENSE file for details.
   

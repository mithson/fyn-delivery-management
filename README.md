

# **Delivery Management System**

This project is a Delivery Management System built using a Django backend and a React.js frontend. The system manages vehicle services, tracks revenue, and provides graphical analytics.

---

## **Features**

1. Operations user can register components with their repair pricing, or new purchase
2. Repair vehicles can be added
3. Issues for the vehicles can be added. Users can choose between new components or
repair
4. Final price Calculation and paying the required amount (Do not go into real-world
transactions)
5. Graphs for Daily, monthly, and yearly revenue. Graphs should be responsive. (library
suggestions - https://recharts.org/en-US/)

---

## **Tech Stack**

- **Backend**: Django, Django REST Framework, CORS Headers.
- **Frontend**: React.js, Axios, Recharts.

---

## **Setup Instructions**

### **1. Backend (Django)**

#### **Prerequisites**

- Python 3.x installed.
- `pip` package manager.
- Virtual environment module (optional but recommended).

#### **Steps**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mithson/fyn-delivery-management.git
   cd fyn-delivery-management/delivery-management
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **API Endpoints**:
   - `http://127.0.0.1:8000/api/vehicles/`: Manage vehicles.
   - `http://127.0.0.1:8000/api/components/`: Manage components.
   - `http://127.0.0.1:8000/api/issues/`: Manage issues.
   - `http://127.0.0.1:8000/api/transactions/`: View transactions.
   - `http://127.0.0.1:8000/api/revenue/`: Fetch revenue data.

---

### **2. Frontend (React.js)**

#### **Prerequisites**

- Node.js and npm installed.

#### **Steps**

1. **Navigate to the frontend folder**:
   ```bash
   cd fyn-delivery-management/delivery-management-frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```

4. **Access the application**:
   Open your browser and navigate to:
   ```plaintext
   http://localhost:3000
   ```

---

## **Backend and Frontend Integration**

To connect the frontend with the backend:
1. Ensure the Django server (`http://127.0.0.1:8000`) is running.
2. Ensure the React.js application (`http://localhost:3000`) is running.
3. The frontend automatically communicates with the backend via Axios.

---

## To allow our react js frontend access django api 

### 1. Adding CORS Policy to our django project 
If you encounter CORS issues, ensure `django-cors-headers` is installed and properly configured in your `settings.py` file:
```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True
```



## **Testing**

### **Backend Testing**
Run Django tests:
```bash
python manage.py test
```

### **Frontend Testing**
Run React tests:
```bash
npm test
```

---

## **Author**

**Abhishek Vishwakarma**  
Round -1 Interview assignment for full stack developer/backend developer role -  Fyn Mobility Bangalore 


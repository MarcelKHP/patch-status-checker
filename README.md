# Patch Status Checker 🔄🖥️

Patch Status Checker is a lightweight web application designed for IT administrators to collect and display patch status across multiple endpoints (Windows, Linux, macOS) via API calls. This tool offers agentless scanning, a dashboard for missing updates, CSV export, and optional integration with WSUS/SCCM.

## Features

- **Agentless Scanning**: Uses WMI for Windows and SSH for Linux/Mac.
- **Dashboard**: Displays missing updates in an easy-to-read format.
- **Export to CSV**: Export patch data to CSV for reporting.
- **Optional Integration**: Integrate with WSUS/SCCM for enhanced functionality.

## Tech Stack

- **Backend**: Python (FastAPI)
- **Frontend**: React
- **Database**: SQLite

## Project Structure

```
patch-status-checker/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.js
│   └── package.json
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- Docker (for deployment)

### Backend Setup

1. Clone the repository:

```sh
git clone https://github.com/yourusername/patch-status-checker.git
cd patch-status-checker/backend
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Run the FastAPI server:

```sh
uvicorn app.main:app --reload
```

### Frontend Setup

1. Navigate to the frontend directory:

```sh
cd ../frontend
```

2. Install the dependencies:

```sh
npm install
```

3. Start the React development server:

```sh
npm start
```

### Deployment

1. Build and run the Docker containers:

```sh
docker-compose up --build
```

2. Access the application at `http://localhost:8000` for the API and `http://localhost:3000` for the frontend.

## Usage

1. **Scanning Endpoints**: Initiate scans for Windows, Linux, and macOS endpoints using the provided API endpoints.
2. **Viewing Patch Status**: Access the dashboard to view the latest patch status and missing updates.
3. **Exporting Data**: Use the export functionality to download patch data in CSV format.
4. **WSUS/SCCM Integration**: Optionally integrate with WSUS/SCCM for extended patch management capabilities.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [marcar82@gmail.com](mailto:marcar82@gmail.com).

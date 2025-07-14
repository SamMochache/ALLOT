## ✅ Frontend Integration Plan (Phase 1 Final Task)

### 1. **Frontend Technology Stack**
- **Framework:** React.js (with Vite for faster build)
- **State Management:** Redux Toolkit
- **UI Styling:** TailwindCSS
- **API Communication:** Axios
- **Charts:** Recharts or D3.js
- **Authentication:** JWT Token handling via React Context or Redux Middleware

### 2. **Frontend Directory Structure**
```
/frontend/
├── src/
│   ├── components/       # Reusable UI components
│   ├── pages/            # Dashboard, Login, Reports etc.
│   ├── services/         # Axios API calls
│   ├── store/            # Redux setup
│   ├── utils/            # Helper functions, token handling
│   └── App.jsx           # App entry point
├── public/
├── tailwind.config.js
├── vite.config.js
```

### 3. **API Endpoints to Integrate**
| API Function           | Endpoint                      | HTTP Method |
|------------------------|-------------------------------|-------------|
| Login / Token          | `/api/token/`                 | POST        |
| Refresh Token          | `/api/token/refresh/`         | POST        |
| List/Create Users      | `/api/users/`                 | GET, POST   |
| List/Create Assessments| `/api/assessments/`           | GET, POST   |
| Vulnerabilities        | `/api/vulnerabilities/`       | GET, POST   |
| Threats                | `/api/threats/`               | GET, POST   |
| Audit Logs             | `/api/audit-logs/`            | GET         |

### 4. **Core Pages to Develop**
- **Login Page**
- **Dashboard:** Summary of risks, assessments, threats
- **Users Management**
- **Assessments Overview & Creation**
- **Vulnerabilities List**
- **Threat Intelligence Feeds**
- **Audit Logs Page**

### 5. **Security Best Practices**
- Securely store JWT tokens (HTTPOnly cookies or secure storage)
- Protect routes using React Router Guards
- Handle token expiration (auto refresh)

### 6. **Deployment Target**
- Develop frontend locally with Vite dev server.
- Build production bundle with:
```bash
npm run build
```
- Serve via Nginx or integrate within Django via **WhiteNoise** or serve separately.

### 7. **Documentation**
Document API consumption in `/docs/frontend_api_usage.md`.

---
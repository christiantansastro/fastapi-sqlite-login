<div align="center">
<h1 align="center">FastAPI SQLite Login System</h1>
</div>

<!-- GETTING STARTED -->
## Getting Started

Instructions on setting up the project locally.
Follow these simple steps.

### Prerequisites

Software needed and how to install them.
* npm
  ```
  npm install npm@latest -g
  ```

### Installation

1. Install packages
   ```
   pip install -r requirements.txt
   ```
2. Run login.js to create SQLite database
   ```
   node login.js
   ```
3. Run FastAPI
   ```
   py -m uvicorn main:app --reload
   ```
4. Run HTTP server
   ```
   http-server
   ```

<!-- USAGE EXAMPLES -->
## Usage
1. Creating SQLite database
![image](https://github.com/christiantansastro/fastapi-sqlite-login/assets/137610891/619c1c1c-cc5d-48d1-bbdc-b711305eaada)

2. Running FastAPI
![image](https://github.com/christiantansastro/fastapi-sqlite-login/assets/137610891/6455f72b-ea65-4341-a775-b52da2d18e81)

3. Running HTTP server

![image](https://github.com/christiantansastro/fastapi-sqlite-login/assets/137610891/af6cb6f5-9d49-4691-a9a0-e3813a505467)

4. When credentials are invalid
![image](https://github.com/christiantansastro/fastapi-sqlite-login/assets/137610891/3e5d0b2f-46ab-4f66-8be4-d3a49e596984)

5. Successful Login
![image](https://github.com/christiantansastro/fastapi-sqlite-login/assets/137610891/949b16c5-8b14-4dd4-8446-dd85970d91e5)

## Note
To not re-authenticate a user each time they navigate a page. It is possible by using a session cookie or JSON Web Token, but for this system, I have not implemented them due to time constraints.

# varonis
To use varonis api python varonis_api.py
POST http://localhost:5000/auth with user and password retuns "token"
after that 
POST http://localhost:5000/normalize with Authorization header set to JWT "token" and data as JSON array

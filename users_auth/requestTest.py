import requests
headers = {}
headers['Authorization'] = 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3NzQwMjg4LCJqdGkiOiJmMzc3MzI2NmQ0NGY0MDA4OGM1YzQzYTg4ZWMwOTMzMiIsInVzZXJfaWQiOjF9.VCmpV7k5KpmjSabUgiEU3Uo7KEBiyr6BfcooKB7gJi8'
r= requests.post('http://localhost:8000/u/jwt/jwt/refresh/', headers=headers)
# r = requests.get('http://127.0.0.1:8000/u/jwt/users/me/', headers=headers)
print(r.text)

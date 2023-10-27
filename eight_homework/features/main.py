from fastapi import FastAPI
import requests

app = FastAPI()


def fetch_user_data(offset):
    url = f'https://sef.podkolzin.consulting/api/users/lastSeen?offset={offset}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        return []


@app.get("/api/reports")
async def get_reports():
    user_data = fetch_user_data(50)

    reports = []

    for user in user_data:
        name = user.get('name_from_url', 'Default Name')
        metrics = user.get('metrics_from_url', [])
        users = user.get('users_from_url', [])

        report = {
            "name": name,
            "metrics": metrics,
            "users": users
        }
        reports.append(report)

    return reports

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="209.97.181.107", port=8000)

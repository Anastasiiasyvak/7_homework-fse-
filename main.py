from fastapi import FastAPI
from datetime import datetime
import requests
import uvicorn


app = FastAPI()

def fetch_user_data(offset):
    url = f'https://sef.podkolzin.consulting/api/users/lastSeen?offset={offset}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        return []

@app.get("/api/stats/user/total")
async def get_total_online_time(user_id: str):
    total_time = calculate_total_online_time(user_id)

    print(f"Total time for user {user_id}: {total_time} seconds")

    return {"totalTime": total_time}

@app.get("/api/stats/user/average")
async def get_average_online_time(user_id: str):
    weekly_average, daily_average = calculate_average_online_time(user_id)

    print(f"Weekly average for user {user_id}: {weekly_average} seconds")
    print(f"Daily average for user {user_id}: {daily_average} seconds")

    return {"weeklyAverage": weekly_average, "dailyAverage": daily_average}

def calculate_total_online_time(user_id: str):
    user_data = fetch_user_data(0)

    total_time = 0

    for user in user_data:
        if user.get('userId') == user_id:
            last_seen_date = user.get('lastSeenDate')
            if last_seen_date:
                last_seen_datetime = datetime.fromisoformat(last_seen_date[:-1])
                current_datetime = datetime.now()
                time_online = current_datetime - last_seen_datetime
                total_time = time_online.total_seconds()
                break

    return total_time

def calculate_average_online_time(user_id: str):
    user_data = fetch_user_data(0)
    daily_total_time = 0
    weekly_total_time = 0
    days_count = 0
    weeks_count = 0
    current_date = datetime.now()

    for user in user_data:
        if user.get('userId') == user_id:
            last_seen_date = user.get('lastSeenDate')
            if last_seen_date:
                last_seen_datetime = datetime.fromisoformat(last_seen_date[:-1])
                time_online = current_date - last_seen_datetime
                total_time = time_online.total_seconds()

                if time_online.days == 0:
                    daily_total_time += total_time
                    days_count += 1

                if time_online.days <= 7:
                    weekly_total_time += total_time
                    weeks_count += 1

    daily_average = daily_total_time / days_count if days_count > 0 else 0
    weekly_average = weekly_total_time / weeks_count if weeks_count > 0 else 0

    return weekly_average, daily_average

@app.get("/api/report/{report_name}")
async def get_report(report_name: str, from_date: str, to_date: str):
    users_data = fetch_user_data(0)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


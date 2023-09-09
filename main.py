from fastapi import FastAPI
from datetime import datetime, timezone
import json 

week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

app = FastAPI()



@app.get('/api')
def stage_config(slack_name: str, track: str):
    response = {
        'slack_name': slack_name,
        'current_day': week_days[int(datetime.now().date().strftime('%w'))],
        'utc_time': datetime.utcnow().replace(tzinfo=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': track,
        'github_file_url': 'https://github.com/elias-dzobo/hngx-backend-stage-one/blob/main/main.py',
        'github_repo_url': 'https://github.com/elias-dzobo/hngx-backend-stage-one',
        'status_code': 200
    }

    return response



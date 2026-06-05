import requests

# Replace this with your real Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1512251932452847768/mKMY-ozHPU0UjHSE7CbUoTKRXmb8I6PpaStKZywYWn93CdxSwdTXzljsDRHWaBA8iUMa"

def send_alert(room_name: str, issue: str, value: float):
    """
    Sends a webhook alert to Discord when a room
    sensor reading exceeds safe thresholds
    """
    message = {
        "content": f"⚠️ ALERT: {room_name} — {issue} (Current reading: {value})"
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=message)
        if response.status_code == 204:
            print(f"Alert sent for {room_name}")
        else:
            print(f"Webhook failed: {response.status_code}")
    except Exception as e:
        print(f"Webhook error: {e}")
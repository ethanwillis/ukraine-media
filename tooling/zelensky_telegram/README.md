# Setup and Running
1. Go to your [Telegram Account](https://my.telegram.org/auth) online.
2. You will be prompted for your phone number.
3. After entering your phone number you will receive a confirmation code in your active Telegram session/client.
4. Create a new app and note the `api_id` and `api_hash` provided for the app.
5. Run this command in this directory: `mv .env.example .env`
6. Open .env in your editor and replace the placeholder values with your `api_id` and `api_hash`
7. Run this command `python3 export.py`
8. Enter your phone number
9. Enter the confirmation code sent to your active Telegram session/client.
10. Now run the following commands `chmod +x run_export.sh` and `./run_export.sh`


# Important Notes
- Telethon creates a file in this directory named 'anon.session' This file allows for a full session for your Telegram account to be used. **Do not share this file**

# Additional Notes
- All output will be saved to [../../archives/zelensky_telegram](../../archives/zelensky_telegram) into a new file with the filename being <current_unix_timestamp>.txt

# Dependencies
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
See: requirements.txt

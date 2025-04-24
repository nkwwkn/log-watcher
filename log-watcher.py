import os, requests, argparse, time

TOKEN = "5528712778:AAG6SCb3jEbBDkBidwsYYobT5h7FC20uRYU"

parser = argparse.ArgumentParser(description="Automatic log parser with notificatoon to Telegram")
parser.add_argument("-tg", action="store_true", help="Enable Telegram notification")
parser.add_argument("-monitor", action="store_true", help="Start program as monitor")
parser.add_argument("--telegram-chat-id", type=str, default="641997529", help="Set Telegram chat id for notification")
parser.add_argument("--level", nargs="+", type=str, default=["ERROR"], help="Set level for notification: ERROR, WARNING, INFO")
parser.add_argument("--input-path", type=str, default="/mnt/c/SAS/app.log", help="Set a log file input path")
parser.add_argument("--filter-dir-path", type=str, default="/mnt/c/SAS/filtered", help="Set a directory path for filtered")
parser.add_argument("--sleep-time", type=int, default="5", help="Set a time sleep for notification")

args = parser.parse_args()

CHAT_ID = args.telegram_chat_id
level = args.level
input_path = args.input_path
directory_path = args.filter_dir_path
sleep_time = args.sleep_time
state_file_path = f"{input_path}.state"




                 
os.makedirs(directory_path, exist_ok=True)

def send_to_telegram(token, chat_id, message):
       url = f"https://api.telegram.org/bot{token}/sendMessage"
       payload = {
        "chat_id": chat_id,
        "text": message
        }
       
       response = requests.post(url, data=payload)

while True:
    new_error_lines = []
    new_info_lines = []
    new_warning_lines = []
    error_count = 0
    last_position = 0
    if os.path.exists(state_file_path):
        with open(state_file_path, "r") as f:
            last_position = int(f.read())
    with open(input_path, "r") as logfile:
           logfile.seek(last_position)
           for line in logfile:
                  if "ERROR" in line:
                         new_error_lines.append(line)
                  if "WARNING" in line:
                         new_warning_lines.append(line)
                  if "INFO" in line:
                         new_info_lines.append(line)
           new_position = logfile.tell()
    with open(state_file_path, "w") as f:
           f.write(str(new_position))
    with open(f"{directory_path}/errors.log","w") as errors:
           errors.writelines(new_error_lines)
    with open(f"{directory_path}/warnings.log","w") as warnings:
           warnings.writelines(new_warning_lines)
    with open(f"{directory_path}/infos.log","w") as infos:
           infos.writelines(new_info_lines)
    logcontent = ""
    if "ERROR" in level:
        error_count += len(new_error_lines)
        logcontent += " ".join(new_error_lines)
    if "WARNING" in level:
        error_count += len(new_warning_lines)
        logcontent += " ".join(new_warning_lines)
    if "INFO" in level:        
        error_count += len(new_info_lines)
        logcontent += " ".join(new_info_lines)
    if args.tg:
           if error_count>0:
                tg_message = f"Логи уровней: {",".join(level)}\nНайдено новых строк: {error_count}\n\n{logcontent[:4000]}"
                send_to_telegram(TOKEN,CHAT_ID,tg_message)
    if not args.monitor:
        break
    time.sleep(sleep_time)
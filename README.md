# Log‑Watcher / Лог‑Вотчер

*A lightweight Python 3 utility for real‑time log filtering and instant Telegram alerts.*  
*Легка утиліта Python 3 для моніторингу логів у реальному часі та миттєвих сповіщень у Telegram.*

---

## ✨ Features / Можливості

| EN | UA |
| --- | --- |
| **Live tailing** — reads a growing log file as it is written, remembering the last byte position across restarts via a `.state` file. | **Читання в реальному часі** — утиліта стежить за файлом журналу, запамʼятовуючи позицію останнього байта у `.state`, тож після перезапуску нічого не втрачається. |
| **Severity routing** — detects `ERROR`, `WARNING`, `INFO` and writes each to its own file inside `--filter-dir-path`. | **Розподіл за рівнями** — рядки з `ERROR`, `WARNING`, `INFO` пишуться у окремі файли в каталозі, заданому `--filter-dir-path`. |
| **Telegram push** — sends any combination of severities to a Telegram chat via the Bot API. | **Сповіщення Telegram** — надсилає обрані типи повідомлень у чат через Bot API. |
| **CLI flags** — flexible control: source file, output folder, severities, chat ID, interval. | **Параметри CLI** — вибір файлу логу, папки, рівнів, чату, інтервалу тощо. |
| **Cross‑platform** — works on Windows 10/11 & Ubuntu 22+. | **Крос‑платформеність** — перевірено на Windows 10/11 та Ubuntu 22+. |

---

## ⚙️  Installation / Встановлення

```bash
python -m pip install -r requirements.txt  # requests>=2.25
```

---

## 🚀  Usage / Приклад запуску

```bash
python logfilter.py \
    --input-path "/var/log/syslog" \
    --filter-dir-path "./filtered" \
    --level ERROR WARNING \
    -tg \
    --telegram-chat-id "123456789" \
    -monitor \
    --sleep-time 5
```

| Flag | Default | EN Description | UA Опис |
|------|---------|----------------|---------|
| `--input-path` | `/mnt/c/SAS/app.log` | Path to the source log file. | Шлях до вхідного файлу журналу. |
| `--filter-dir-path` | `/mnt/c/SAS/filtered` | Folder for filtered logs. | Каталог для відфільтрованих логів. |
| `--level` | `ERROR` | Severities to capture (`ERROR`, `WARNING`, `INFO`). | Рівні, які слід перехоплювати. |
| `-tg` | off | Enable Telegram alerts. | Увімкнути сповіщення Telegram. |
| `--telegram-chat-id` | `641997529` | Chat ID to send messages. | ID чату для надсилання повідомлень. |
| `-monitor` | off | Run continuously, otherwise exits after first pass. | Працювати безперервно, інакше вихід після одного проходу. |
| `--sleep-time` | `5` | Seconds between scans when in monitor mode. | Пауза між перевірками в режимі моніторингу. |

---

## 📄  License / Ліцензія

MIT  
Вихідний код відкритий під ліцензією MIT — вільно використовуйте й модифікуйте.

---

> Created as a pet‑project and showcased in my CV.  
> Створено як pet‑проєкт і додано до мого резюме.


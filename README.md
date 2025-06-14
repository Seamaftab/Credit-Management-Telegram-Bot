## Credit-Management-Telegram-Bot

A Telegram bot for managing user credits via Supabase. It supports user and admin commands for creating, checking, renewing credits, and managing tokens.

---

## 📌 Features

✅ **User Commands:**

* **/create** — Create a new credit token and send request to admin
* **/credits** — Check your current credits
* **/demo** — Generate a 1-day demo token (one time only)
* **/renew** — Renew an existing token for additional days (min 5 days)

✅ **Admin Commands:**

* **/add** — Add credit days to a user
* **/set** — Set/reset a user’s credits
* **/credits** — Check credits for a specific user or all users

✅ Uses [Supabase](https://supabase.io) for secure and scalable database storage.

---

## ⚙️ Configuration

The bot is configured via `config.json`:

```json
{
  "admins": ["<admin_id_or_username>", "SeamAftab"],
  "user": ["Edward"],
  "telegram_bot_token": "<your_telegram_bot_token>",
  "supabase_url": "<your_supabase_url>",
  "supabase_key": "<your_supabase_key>"
}
```

* Replace placeholders with your actual Telegram bot token and Supabase credentials.
* Add admin usernames/IDs as needed.

---

## 🏗️ Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/Credit-Management-Telegram-Bot.git
cd Credit-Management-Telegram-Bot
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

*(Create `requirements.txt` if missing. Example content:)*

```
pyTelegramBotAPI
supabase
```

3️⃣ **Configure the bot**

* Edit `config.json` with your bot token, Supabase URL & key, and admin/user details.

---

## ▶️ Usage

Run the bot:

```bash
python main.py
```

The bot will listen for commands and interact with users via Telegram.

---

## 🧑‍💻 Commands Menu

Users can easily use commands through the Telegram chat menu.
Example commands:

* `/create`
* `/credits`
* `/demo`
* `/renew`

---

## ✅ Example Commands

```
token Pedro 6939262788f8 10
renew 6939262788f8 15
```

---

## 🤝 Contributing

Feel free to fork and contribute!
For major changes, open an issue first to discuss what you would like to change.

---

## 📄 License

Specify your license here (e.g., MIT License).

---

## 📬 Contact

For questions or help, contact the admin listed in `config.json`.

---

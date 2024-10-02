import json
from database import *
from datetime import datetime, timedelta

def config_file():
    with open('config.json') as file:
        return json.load(file)

config = config_file()

def handle_create(message, bot):
    username = message.from_user.username
    msg = bot.send_message(message.chat.id, f"@{username}, Your Token Please")
    bot.register_next_step_handler(msg, process_token_step, bot)

def process_token_step(message, bot):
    token = message.text
    msg = bot.send_message(message.chat.id, "How many days of credits? (5 minimum)")
    bot.register_next_step_handler(msg, process_days_step, bot, token)

def process_days_step(message, bot, token):
    try:
        days = int(message.text)
        if days < 5:
            bot.send_message(message.chat.id, "The minimum number of credit days is 5. Please try again.")
            return

        username = message.from_user.username
        add_user(username, token, days)
        forward_to_admin(bot, username, token, days)
        bot.send_message(message.chat.id, "Your request has been forwarded to the admin.")
    
    except ValueError:
        bot.send_message(message.chat.id, "Please provide a valid number of days.")

def forward_to_admin(bot, username, token, days):
    admin = config['admins'][0]
    bot.send_message(admin, f"New user request:\nUsername: {username}\nToken: {token}\nDays: {days}")

def handle_credits(message, bot):
    username = message.from_user.username

    if username not in config['admins']:
        credits = get_user_credits(username)
        if credits is not None:
            bot.send_message(message.chat.id, f"Your credits: {credits}")
        else:
            bot.send_message(message.chat.id, "Could not find your credits.")
    else:
        msg = bot.send_message(message.chat.id, f"@{username}, enter username (or 'all' to check all users and credits).")
        bot.register_next_step_handler(msg, handle_credits_by_admin, bot)

def handle_credits_by_admin(message, bot):
    target_username = message.text.strip()
    all_users = get_all_users()
    
    if target_username == "all":
        response = "\n".join([f"{user}: {credits}" for user, credits in all_users.items()])
        bot.send_message(message.chat.id, response)
    else:
        credits = get_user_credits(target_username)
        if credits is not None:
            bot.send_message(message.chat.id, f"Credits for {target_username}: {credits}")
        else:
            bot.send_message(message.chat.id, "User not found.")

def handle_demo(message, bot):
    username = message.from_user.username
    
    if check_demo_token(username):
        credits = get_user_credits(username)
        bot.send_message(message.chat.id, f"You already have {credits} token. You cannot generate another demo.")
        return None
    
    demo_token = generate_demo_token(username)

    if demo_token:
        bot.send_message(message.chat.id, f"{username}, Your demo token is: {demo_token}. It is valid for 1 day.")
    else:
        bot.send_message(message.chat.id, "Failed to generate a demo token. Please try again later.")

    return None

def handle_renew(message, bot):
    msg = bot.send_message(message.chat.id, "Please insert your token")
    bot.register_next_step_handler(msg, token_for_renewal, bot)

def token_for_renewal(message, bot):
    token = message.text

    if check_token(token):
        msg = bot.send_message(message.chat.id, "How many days would you like to renew? (5 minimum)")
        bot.register_next_step_handler(msg, days_for_renewal, bot, token)
    else:
        bot.send_message(message.chat.id, "Token not found. Please try again with a valid token.")

def days_for_renewal(message, bot, token):
    try:
        days = int(message.text)
        if days < 5:
            bot.send_message(message.chat.id, "The minimum number of days for renewal is 5. Please try again.")
            return

        success = renew_token(token, days)
        if success:
            bot.send_message(message.chat.id, f"Token {token} has been renewed for {days} days.")
        else:
            bot.send_message(message.chat.id, "Failed to renew the token. Please try again.")
    
    except ValueError:
        bot.send_message(message.chat.id, "Please provide a valid number of days.")

def handle_admin_commands(message, bot):
    user_id = message.from_user.id
    admin_command = message.text.strip().lower()

    if user_id not in config['admins']:
        bot.send_message(message.chat.id, "You are not authorized to access this command.")
    else:
        msg = bot.send_message(message.chat.id, "Insert username.")
        bot.register_next_step_handler(msg, process_user_and_credits, bot, admin_command)

def process_user_and_credits(message, bot, admin_command):
    username = message.text.strip()

    if username in get_all_users():
        msg = bot.send_message(message.chat.id, "Enter credit days.")
        bot.register_next_step_handler(msg, process_credits, bot, admin_command, username)
    else:
        bot.send_message(message.chat.id, f"{username} not found.")

def process_credits(message, bot, admin_command, username):
    admin_command = admin_command
    #print(admin_command)
    try:
        days = int(message.text.strip())
        
        if admin_command == "/add":
            update_user_credits(username, days)
            bot.send_message(message.chat.id, f"Successfully added {days} days to {username}'s credits.")
        elif admin_command == "/set":
            set_user_credits(username, days)
            bot.send_message(message.chat.id, f"Successfully set {username}'s credits to {days} days.")
        else:
            bot.send_message(message.chat.id, "Invalid admin command. Use 'add' or 'set'.")
    except ValueError:
        bot.send_message(message.chat.id, "Please provide a valid number of days.")


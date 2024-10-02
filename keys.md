The client wants to develop a **Credit Management Telegram Bot** that can manage user credits with both **admin** and **user** commands, controlled through a config file. The database system should be on Supabase.

### Key details:
- **Config file**: Contains admin usernames, destination user, and group usernames. Admins can be hardcoded with their user IDs or usernames.
  
- **Admin Commands**:
  - **Credits**: Lists all users' credits or, if a specific user is provided, lists only their credits.
  - **Add**: Adds credit to a specified user.
  - **Set**: Sets or resets the credit for a user (set to 0 to remove credits).

- **User Commands**:
  - **Create**: Collects a username, token, and credit days (min 5) and  `token` is also given by user. and forward this new message to the admin.
  - **Credits**: Checks his credits.
  - **Demo**: Generates a token for a demo session, valid for 1 day. Only applicable once per username.
  - **Renew**: Takes a token ID and a number of days (min 5) to renew the token, generating a `renew` command.

### Expected Output:
The bot needs to generate commands like:
- **token Pedro 6939262788f8 10**
- **renew 6939262788f8 15**

### Work Style : 
- **Menu for the commands**
  ***Example*** : the bottom left part of the chat box of telegram have he menu button, clicking it would should show "/create", "/Credits", "/demo", "/Renew", clicking one of them would trigger a command, then the response/question for following info will follow.
- **Example** : `User` calling `create` would ask him for `token` and then ask for `days`, of course we will verify it, read the `username`, and store it in supabase table `credits`
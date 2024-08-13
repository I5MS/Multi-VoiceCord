# Mutli-VoiceCord

This project contains a Python script (`main.py`) that manages the execution of multiple Discord accounts, each running in its own script (`app1.py`, `app2.py`, `app3.py`, and `app4.py`). The accounts are set to reconnect to a specific voice channel every 6 hours.

## Disclaimer: 
 This project breaks Discord’s rules and may get your account banned. 

## Warning: 
 Don’t share your Discord token with anyone, as it lets them access your account, including bypassing two-factor authentication (2FA) and your password.

## Project Structure

- **main.py**: The main script responsible for launching and managing the accounts.
- **app1.py to app4.py**: Individual account scripts that connect to a specified Discord voice channel.
- **requirements.txt**: Lists all the Python packages required for the account to run.

## How It Works

- The `main.py` script runs an infinite loop where it:
  1. Terminates any previously running account processes.
  2. Clears the list of those processes.
  3. Launches each account script (`app1.py` to `app4.py`).
  4. Waits for 6 hours (21,600 seconds) before restarting the accounts.

- Each account script (`app1.py` to `app4.py`) uses the Discord API to:
  1. Log in to Discord using the provided token.
  2. Connect to a specified voice channel.

## Setup Instructions

### Prerequisites

- Python 3.8
- Discord account Tokens for each app.

### Installation

1. **Clone the repository** (or download the script):
    ```bash
    git clone https://github.com/i5ms/Multi-VoiceCord.git
    cd Multi-VoiceCord
    ```

2. **Install the required dependencies** using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Replace `Your_Token_Here`** in `app1.py` to `app4.py` with your actual Discord account token(s).

4. **Replace `1111111111111111111`** in each account script with the ID of the Discord voice channel you want the accounts to connect to.

### Running the Accounts

- Run the `main.py` script to start the accounts:
    ```bash
    python main.py
    ```

- The accounts will automatically restart every 6 hours.

### Notes

- Ensure that each account has the necessary permissions to connect to the voice channel.
- If you have multiple tokens, use a different one for each `app(X).py` script.

### Troubleshooting

- **Accounts not connecting to the voice channel**: Double-check the channel ID and the account's permissions.
- **Script not running**: Ensure that your Python environment is set up correctly and all dependencies are installed.

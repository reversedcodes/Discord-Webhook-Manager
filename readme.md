
# Discord Webhook Manager

**Discord Webhook Manager** is a Python-based tool designed for creating, viewing, editing, and deleting Discord webhooks. This repository is ideal for developers who want to manage webhooks for advanced functionalities like sending interactive messages with buttons in Discord.

## Features

- **Create Webhooks**  
  Easily create new webhooks in any Discord channel by providing the channel ID and a custom webhook name.

- **View All Webhooks**  
  Retrieve and display all webhooks in a specific channel, including their IDs, names, and URLs.

- **Edit Webhooks**  
  Modify the name of an existing webhook.

- **Delete Webhooks**  
  Permanently delete webhooks by their ID.

- **Interactive Menu**  
  A user-friendly menu guides you through all available actions step-by-step.

## Use Case

This tool is particularly useful for:
- Setting up webhooks to send messages with interactive buttons or components.
- Managing existing webhooks efficiently for your Discord bot integrations.
- Debugging or maintaining webhooks in Discord servers.

By leveraging the webhooks created with this tool, developers can implement advanced Discord functionalities, such as:
- Sending messages with buttons, links, and dropdowns.
- Automating message delivery to specific channels.

## Requirements

1. **Python 3.7+**  
2. **Dependencies**  
   Install the required Python library:
   ```bash
   pip install requests
   ```

3. **A Discord Bot**  
   - The bot must have the `Manage Webhooks` permission in the target Discord server.

4. **Discord Channel ID**  
   - Enable Developer Mode in Discord to copy the Channel ID.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/discord-webhook-manager.git
   cd discord-webhook-manager
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Run the script:
   ```bash
   python webhook_manager.py
   ```

## Usage

1. Enter your bot token when prompted.
2. Choose an action from the interactive menu:
   - Create, view, edit, or delete webhooks.
3. Follow the prompts to provide necessary inputs like Channel ID, Webhook ID, or Webhook name.

## Example

### Menu Preview:
```plaintext
Discord Webhook Manager
1. List all webhooks
2. Edit a webhook
3. Create a webhook
4. Delete a webhook
5. Exit
Choose an option: _
```

### Example Output:
```
[+] Webhook successfully created: https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN
```

## Future Enhancements

- Add support for interactive webhook messages with buttons and dropdown menus.
- Implement avatar management for webhooks.
- Add logging for webhook operations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

import requests

def get_all_webhooks(bot_token, channel_id):
    response = requests.get(
        url=f"https://discord.com/api/v10/channels/{channel_id}/webhooks",
        headers={
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json"
        }
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch webhooks: {response.status_code} - {response.text}")


def edit_webhook(bot_token, webhook_id, new_name=None):
    payload = {}
    if new_name:
        payload["name"] = new_name

    response = requests.patch(
        url=f"https://discord.com/api/v10/webhooks/{webhook_id}",
        headers={
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to edit webhook: {response.status_code} - {response.text}")


def delete_webhook(bot_token, webhook_id):
    response = requests.delete(
        url=f"https://discord.com/api/v10/webhooks/{webhook_id}",
        headers={
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json"
        }
    )
    if response.status_code == 204:
        print(f"Webhook {webhook_id} deleted successfully.")
    else:
        raise Exception(f"Failed to delete webhook: {response.status_code} - {response.text}")


def create_webhook(bot_token, channel_id, webhook_name):
    response = requests.post(
        url=f"https://discord.com/api/v10/channels/{channel_id}/webhooks",
        headers={
            "Authorization": f"Bot {bot_token}",
            "Content-Type": "application/json"
        },
        json={"name": webhook_name}
    )
    if response.status_code in [200, 201]:
        return response.json()["url"]
    else:
        raise Exception(f"Failed to create webhook: {response.status_code} - {response.text}")


def menu(bot_token):
    while True:
        print("\nDiscord Webhook Manager")
        print("1. List all webhooks")
        print("2. Edit a webhook")
        print("3. Create a webhook")
        print("4. Delete a webhook")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                channel_id = input("Channel ID: ").strip()
                webhooks = get_all_webhooks(bot_token, channel_id)
                print("Webhooks found:")
                for webhook in webhooks:
                    print(f"ID: {webhook['id']}, Name: {webhook['name']}, URL: {webhook['url']}")

            elif choice == "2":
                webhook_id = input("Webhook ID: ").strip()
                new_name = input("New name (leave blank to skip): ").strip() or None
                webhook = edit_webhook(bot_token, webhook_id, new_name=new_name)
                print(f"Webhook updated successfully: {webhook}")

            elif choice == "3":
                channel_id = input("Channel ID: ").strip()
                webhook_name = input("Webhook Name: ").strip()
                webhook_url = create_webhook(bot_token, channel_id, webhook_name)
                print(f"Webhook created successfully: {webhook_url}")

            elif choice == "4":
                webhook_id = input("Webhook ID: ").strip()
                delete_webhook(bot_token, webhook_id)

            elif choice == "5":
                print("Exiting.")
                break

            else:
                print("Invalid option.")

        except Exception as e:
            print(str(e))


def main():
    bot_token = input("Bot Token: ").strip()
    menu(bot_token)


if __name__ == "__main__":
    main()

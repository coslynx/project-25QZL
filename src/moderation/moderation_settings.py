# File: src/moderation/moderation_settings.py (Python)

# Import necessary packages
import json
import os

# Define the ModerationSettings class
class ModerationSettings:
    def __init__(self):
        self.settings = {}

    def load_settings(self):
        try:
            with open('settings.json', 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            # Create a new settings file if it doesn't exist
            self.save_settings()

    def save_settings(self):
        with open('settings.json', 'w') as file:
            json.dump(self.settings, file, indent=4)

    def update_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def get_setting(self, key):
        return self.settings.get(key, None)

# Instantiate the ModerationSettings object
moderation_settings = ModerationSettings()
moderation_settings.load_settings()
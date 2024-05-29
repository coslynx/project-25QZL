# logging_system.py (Python)

import logging
import json
from datetime import datetime

class LoggingSystem:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger('discord_logger')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_action(self, action, user_id, server_id):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - User {user_id} performed {action} in server {server_id}'
        self.logger.info(log_message)

    def log_warning(self, user_id, server_id, reason):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - Warning issued to user {user_id} in server {server_id}: {reason}'
        self.logger.warning(log_message)

    def log_mute(self, user_id, server_id, duration):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - User {user_id} muted in server {server_id} for {duration} seconds'
        self.logger.info(log_message)

    def log_kick(self, user_id, server_id, reason):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - User {user_id} kicked from server {server_id} for: {reason}'
        self.logger.info(log_message)

    def log_ban(self, user_id, server_id, reason):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - User {user_id} banned from server {server_id} for: {reason}'
        self.logger.info(log_message)

    def log_auto_moderation(self, action, user_id, server_id):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - Auto moderation: {action} performed on user {user_id} in server {server_id}'
        self.logger.info(log_message)
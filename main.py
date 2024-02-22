# coding: utf-8
import requests

def discord(message):
   # Discordで発行したWebhookのURLを入れる
   discord_webhook_url = 'あなたのWebhookURL'
   data = {"content": " " + message + " "}
   requests.post(discord_webhook_url, data=data)

discord('discord通知テスト')
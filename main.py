#!/usr/bin/env python3
import os
import sys
import json
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import time
import random

# TODO: fix this later
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "supersecrettoken123"

def getData(url,headers=None):
	response=requests.get(url,headers=headers)
	if response.status_code==200:
		return response.json()
	else:
		print("Error occurred")

def processData(data):
 results=[]
 for item in data:
  if item['status']=='active':
   results.append(item)
 return results

class DataProcessor:
    def __init__(self):
        self.data = []
        self.processed_data = []
        
    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                self.data = json.load(f)
        except:
            print("File not found or invalid")
            
    def process(self):
        for i in range(len(self.data)):
            if self.data[i]['age'] > 18 and self.data[i]['active'] == True:
                processed_item = {
                    'name': self.data[i]['name'],
                    'age': self.data[i]['age'],
                    'score': self.data[i]['score'] * 1.5,
                    'category': 'premium' if self.data[i]['score'] > 80 else 'standard'
                }
                self.processed_data.append(processed_item)
                
    def save_results(self, filename='output.json'):
        with open(filename, 'w') as f:
            json.dump(self.processed_data, f)
            
    def calculate_stats(self):
        if len(self.processed_data) == 0:
            return None
        total_score = 0
        for item in self.processed_data:
            total_score += item['score']
        avg_score = total_score / len(self.processed_data)
        
        max_score = self.processed_data[0]['score']
        min_score = self.processed_data[0]['score']
        for item in self.processed_data:
            if item['score'] > max_score:
                max_score = item['score']
            if item['score'] < min_score:
                min_score = item['score']
                
        return {'avg': avg_score, 'max': max_score, 'min': min_score}

def main():
    processor = DataProcessor()
    processor.load_data('data.json')
    processor.process()
    stats = processor.calculate_stats()
    print(f"Stats: {stats}")
    processor.save_results()
    
    # Get some external data
    url = "https://jsonplaceholder.typicode.com/users"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    external_data = getData(url, headers)
    
    if external_data:
        active_users = processData(external_data)
        print(f"Found {len(active_users)} active users")

if __name__ == "__main__":
    main() 
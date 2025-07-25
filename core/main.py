#!/usr/bin/env python3
import json
import requests
import config

class DataProcessor:
    def __init__(self):
        self.data = []
        self.processed_data = []

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Invalid JSON in '{filename}'.")

    def process_data(self):
        for item in self.data:
            if item.get('age', 0) > 18 and item.get('active', False):
                processed_item = {
                    'name': item['name'],
                    'age': item['age'],
                    'score': item['score'] * 1.5,
                    'category': 'premium' if item['score'] > 80 else 'standard'
                }
                self.processed_data.append(processed_item)

    def save_results(self, filename='output.json'):
        with open(filename, 'w') as f:
            json.dump(self.processed_data, f)

    def calculate_stats(self):
        if not self.processed_data:
            print("No processed data available.")
            return None

        scores = [item['score'] for item in self.processed_data]
        return {
            'avg': sum(scores) / len(scores),
            'max': max(scores),
            'min': min(scores)
        }
    
def get_data(url,headers=None):
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		return response.json()
	else:
		print(f"Request failed with status code: {response.status_code}.")
          

def filter_active_users(data):
     return [user for user in data if user.get('status') == 'active']


def main():
    processor = DataProcessor()
    processor.load_data('data.json')
    processor.process_data

    stats = processor.calculate_stats()
    if stats:
        print(f"Stats: {stats}")
    processor.save_results()
    
    # Get some external data
    url = "https://jsonplaceholder.typicode.com/users"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    external_data = get_data(url, headers)
    
    if external_data:
        active_users = filter_active_users(external_data)
        print(f"Found {len(active_users)} active users.")

if __name__ == "__main__":
    main() 




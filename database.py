import json
import random
from supabase import create_client, Client

def connect_to_supabase():
    with open('config.json') as file:
        config = json.load(file)

    url = config['supabase_url']
    key = config['supabase_key']

    return create_client(url, key)

def add_user(username, token, days):
    supabase = connect_to_supabase()
    data = {
        'username': username,
        'credits': days,
        'token': token
    }
    response = supabase.table('credits').insert(data).execute()
    return response

def get_user_credits(username):
    supabase = connect_to_supabase()
    response = supabase.table('credits').select('credits').eq('username', username).execute()
    
    if response.data:
        return response.data[0]['credits']
    return None

def set_user_credits(username, credits):
    supabase = connect_to_supabase()
    response = supabase.table('credits').update({'credits': credits}).eq('username', username).execute()
    return response

def update_user_credits(username, credits):
    supabase = connect_to_supabase()
    
    current_credits_response = supabase.table('credits').select('credits').eq('username', username).execute()
    if current_credits_response.data:
        current_credits = current_credits_response.data[0]['credits']
        new_credits = current_credits + credits
        
        response = supabase.table('credits').update({'credits': new_credits}).eq('username', username).execute()
        return response
    else:
        return None

def check_token(token):
    supabase = connect_to_supabase()
    response = supabase.table('credits').select('token').eq('token', token).execute()
    
    if response.data:
        return True
    return False

def check_demo_token(username):
    supabase = connect_to_supabase()
    response = supabase.table('credits').select('token').eq('username', username).execute()
    
    return bool(response.data)

def generate_demo_token(username):
    supabase = connect_to_supabase()
    demo_token = 'g-' + ''.join(random.choices('0123456789', k=9))
    data = {
        'username': username,
        'credits': 1,
        'token': demo_token
    }
    response = supabase.table('credits').insert(data).execute()
    return response

def renew_token(token, days):
    supabase = connect_to_supabase()
    
    token_response = supabase.table('credits').select('credits').eq('token', token).execute()
    
    if token_response.data:
        current_days = token_response.data[0]['credits']
        new_days = current_days + days
        
        response = supabase.table('credits').update({'credits': new_days}).eq('token', token).execute()
        return response
    else:
        return False

def get_all_users():
    supabase = connect_to_supabase()
    response = supabase.table('credits').select('username, credits').execute()
    
    if response.data:
        users_credits = {user['username']: user['credits'] for user in response.data}
        return users_credits
    return {}

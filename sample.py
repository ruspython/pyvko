import vk
import json

APP_ID = '3313789'
SCOPE = '8388607' #all (sum([2**x for x in range(23)])) 
mytoken, user_id = vk.auth(email='vlad0058@gmail.com', password='%8h\'T+Wj1', client_id=APP_ID, scope=SCOPE)
print('\n', mytoken, user_id)
d = {'user_id': user_id, 'count':'14'}
json_obj = json.loads(vk.method_request(token=mytoken, method_name='audio.get', params=d).decode())

print(json_obj['response'])

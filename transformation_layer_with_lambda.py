import base64
import json

def lambda_handler(event, context):
    output_records = []

    for record in event['records']:
        
        try:
            
            payload = base64.b64decode(record['data'])
            payload_json = json.loads(payload)

            
            dynamodb_data = payload_json['dynamodb']
            new_image = dynamodb_data['NewImage']
            print(new_image)

            
            transformed_data = {
                'orderid': new_image['orderid']['S'],
                'product_name': new_image['product_name']['S'],
                'quantity': int(new_image['quantity']['N']),
                'price': float(new_image['price']['N'])
            }

            
            transformed_data_str = json.dumps(transformed_data) + '\n'
            transformed_data_encoded = base64.b64encode(transformed_data_str.encode('utf-8')).decode('utf-8')

            
            output_records.append({
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': transformed_data_encoded
            })

        except Exception as e:
            
            output_records.append({
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']  
            })

    return {
        'records': output_records
    }

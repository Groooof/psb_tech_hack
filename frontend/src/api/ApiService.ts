import { IPostDataEntity } from './types';

const _apiUrl = 'http://10.201.133.185/api/v1/choose_credits';
    
export async function postData(data: IPostDataEntity) {
    return await fetch(_apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    
}
from utils import get_completion_from_messages

def do_trans(input):
    messages =  [  
        {'role':'system', 'content':'你是一个语言翻译助手, 根据```标记的文字翻译成中文韩文英文日文并转换成JSON输出。'},    
        {'role':'system', 'content':'如果要翻译的目标文字和标记文字语种一致则对应的翻译输出为原标记文字输出。'},    
        {'role':'user', 'content':'```hello```'},   
        {'role':'assistant', 'content':'{"en":"hello", "ko":"안녕하세요", "cn": "你好", "jp":"こんにちは"}'},   
        {'role':'user', 'content':'```' + input + '```'}  
    ]
    result = get_completion_from_messages(messages)
    print(result)
    return result
from utils import get_completion_from_messages

def do_trans(input):
    messages =  [  
        {'role':'system', 'content':'你是一个语言翻译助手, 根据```标记的文字翻译成中文韩文英文日文并转换成JSON输出。'},    
        {'role':'system', 'content':'如果翻译的目标语种和标记文字语种一致则这个目标语种不需要翻译输入原标记文字。其他语种继续翻译。'},
        {'role':'user', 'content':'```hello```'},   
        {'role':'assistant', 'content':'{"en":"hello", "ko":"안녕하세요", "cn": "你好", "jp":"こんにちは"}'},   
        {'role':'user', 'content':'```' + input + '```'}  
    ]
    result = get_completion_from_messages(messages)
    print(result)
    return result